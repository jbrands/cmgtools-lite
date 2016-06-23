from __future__ import print_function
import subprocess as sp
import shutil
import multiprocessing as mp
import numpy as np
import shlex
import time
import os
import sys



#Copy, Merge and Count Handler
class CMCHandler():
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

    def getTrees(self):
        
        sub_folders = []
        for i in xrange(6):
            proc = sp.Popen(["dpns-ls {0}".format(self.source)], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
            (out, err) = proc.communicate()
            strout = out.split('\n')
            if '0000' in strout:
                sub_folders = strout[:-1]
                break

            self.source += '/{0}'.format( strout[0] )

        files = {}
        for folder in sub_folders:
            path = "{0}/{1}".format( self.source, folder )
            proc = sp.Popen(['dpns-ls {0}'.format( path ) ], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
            (out, err) = proc.communicate()
            files[folder] ={}
            files[folder]['path'] = path
            files[folder]['files'] = out.split('\n')[:-1]

        return files

    def copyFiles(self,ftype, sub = 'all', force = False,max_proc = 4):



        if os.path.exists(self.dest) and not force:
            print( '{0} already exists'.format(self.dest) )
            sys.exit()
        elif ftype != 'tree' and ftype != 'Skim':
            print( 'Use \'Skim\' or \'tree_\' as ftype!!!' )
            sys.exit()
        elif not os.path.exists(self.dest) and force:
            os.mkdir( self.dest )
        elif not force:
            os.mkdir( self.dest )
        
        trees = self.getTrees()
        cp_cmd = 'lcg-cp srm://hephyse.oeaw.ac.at'
        cmd_list = []
        for folder in trees:
            path = trees[folder]['path']

            if sub == 'all' or sub == folder:
                for file in trees[folder]['files']:
                    if ftype in file:
                        cmd_list.append('{0}/{1}/{2} {3}/{4}'.format(
                                            cp_cmd,
                                            path,
                                            file,
                                            self.dest,
                                            file.replace('tree_','tree_unmerged_')
                                            )
                                        )

        # if ftype == 'tree':
        print( 'Start copying {0} files'.format(ftype) )
        self.applyCmdMulti( cmd_list,  max_proc=max_proc)
        print( '\nFinished' )
        # elif ftype == 'Skim':
        #     self.ApplyCmd( cmd_list )



    def getSkimCount(self):
        strSrch = 'Sum Unity Weights'
        events = 0
        for file in os.listdir(self.dest):
            if 'Skim' in file:

                with open('{0}/{1}'.format(self.dest, file) ,'r') as FSO:
                    strLines = FSO.readlines()
                for strLine in strLines:
                    if strSrch in strLine:
                        strLine = strLine.split('\t')
                        if strSrch in strLine[1]:
                            events += float(strLine[1].replace( strSrch, '' ))

        with open( '{0}/NEvents.txt'.format(self.dest), 'w' ) as FSO:
            FSO.write('Total Number of events: {0}'.format( events ))

        print( 'Created NEvents.txt' )
        return events



    def mergeTrees(self):
        unmerged = []
        for file in os.listdir(self.dest):
            if 'unmerged' in file:
                unmerged.append( [file,int(file.replace('.root','').replace('tree_unmerged_','')) ] )  

        unmerged = np.array(unmerged)
        unmerged = unmerged[ np.array(unmerged[:,1],dtype='int').argsort() ]

        off = 1
        if len(unmerged) < int(unmerged[-1,1]):
            index = len(unmerged)
        else:
            index = int(unmerged[-1,1])

        cmd_list =[]
        strCmd = ''

        mtree = 1
        for i in xrange( index ):
            
            if unmerged[i,1] != str(i+off):
                while unmerged[i,1] != str(i+off):
                    off+=1

            strCmd += ' {0}/{1}'.format(self.dest, unmerged[i,0] )

            if str(i+off)[-1] == '9':

                cmd_list.append('hadd {0}/tree_merged_{1}.root {2}'.format(self.dest, mtree, strCmd ) )
                mtree += 1
                strCmd = ''

            elif i == index-1:
                cmd_list.append('hadd {0}/tree_merged_{1}.root {2}'.format(self.dest, mtree, strCmd ) )

        print( 'Start merging files' )
        self.applyCmdMulti( cmd_list, max_proc=4 )



    def exec_cmd(self,cmd, q):
        p = sp.Popen(shlex.split(cmd), shell=False)
        p.wait()
        q.put(object)


    def applyCmdMulti(self,cmd_list, max_proc=4):
        count = 0
        done_queue = mp.Queue()
        for i, cmd in enumerate(cmd_list):
            if i >= max_proc:
                done_queue.get(block=True)
            proc = mp.Process(target=self.exec_cmd, args=(cmd, done_queue))
            proc.start()
            if i == len(cmd_list)-1:
                proc.join()

            if 'lcg-cp' in cmd:
                count += 1
                print('*', end='')
                if (i+1) % 50 == 0:
                    print('  50')
                    count = 0
                elif i == len(cmd_list)-1:
                    print('{0}{1}'.format(' '*(52-count), count) )

    def cleanup(self):
        print('Removing unneeded Files')
        skimfiles = []
        for file in os.listdir(self.dest):
            if 'unmerged' in file:
                print('*', end='')
                os.remove('/'.join( [self.dest,file] ) )
            if 'Skim' in file:
                skimfiles.append(file)

        if not os.path.exists( '/'.join([self.dest,'Skimreport']) ):
            os.mkdir( '/'.join([self.dest,'Skimreport']) )

        print('\nMoving Skimfiles')
        for file in skimfiles:
            print('*',end="")
            shutil.move( '/'.join([self.dest,file]), '/'.join([self.dest,'Skimreport',file]))
        print('\nFinished')





if __name__ == '__main__':

    source = '/dpm/oeaw.ac.at/home/cms/store/user/mspanrin/cmgTuples/VVTo2L2Nu_MCFall15_160407'
    dest = '/data/mspanring/cmgtools/test'

    ch = CMCHandler(source, dest)
    ch.copyFiles(ftype = 'tree')

    ch.copyFiles(ftype = 'Skim',
                 force = True,
                 max_proc=8)

    ch.getSkimCount()
    ch.mergeTrees()
    ch.cleanup()




