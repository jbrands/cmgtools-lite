import os
import sys
import argparse
import time
import json
from subprocess import Popen, PIPE


def getCrabFolders(paths):

    crab_folders = []
    for path in paths:
        for folder in os.listdir(path):
            if os.path.isdir( '/'.join([ path, folder ]) ) and 'crab_' in folder:

                crab_folders.append( '/'.join([ path, folder ]) )
    return crab_folders

def readInformationFile():
    if not os.path.exists('job_information.dat'):
        open('job_information.dat','a').close()
        return []  
    else:
        with open('job_information.dat','r') as FSO:
            info_content = FSO.read().splitlines()
        return info_content

def addInformation(folders, information):
    add_folder =[]
    for folder in folders:
        exists = False
        for info in information:
            if folder in info:
                exists = True
        if not exists:
            add_folder.append( folder )

    for folder in add_folder:
        information.append( ';{0};0;0'.format(folder) )

    return information

def removeInformation(folders, information):

    for i,info in enumerate(information):
        exists = False
        for folder in folders:
            if folder in info:
                exists = True
        if not exists:
            information.pop(i)

    return information



def updateInformationFile(paths, RESUB = True):
    crab_folders = getCrabFolders(paths)
    info_content = readInformationFile()
    if info_content == []:
        for folder in crab_folders:
            info_content.append( ';{0};0;0'.format(folder) )

        with open('job_information.dat','w') as FSO:
            FSO.write( '\n'.join(info_content) )

    else:
        if os.path.isfile('das_urls.json'):
            with open('das_urls.json','rb') as FSO:
		das_urls = json.load(FSO)
        else:
            with open('das_urls.json','wb') as FSO:
		json.dump({}, FSO)
		das_urls = {}
        
        info_content = addInformation(crab_folders, info_content)
        info_content = removeInformation(crab_folders, info_content)

        print '{0}\n{1}RUNNING'.format( '-'*80, ' '*25 )

        completed_jobs = []
        failed_jobs = []
        for i,info in enumerate(info_content):

            if info != '':
                splInfo = info.split(';')
                job_name = splInfo[1].split('/')[-1].replace('crab_','')
            else:
                continue

            if splInfo[0] == 'COMPLETED':
                completed_jobs.append( job_name )

            elif splInfo[0] == 'FAILED':
                failed_jobs.append( job_name )

            else:
                status, das_url = getStatus( splInfo[1] )
                if status == 'COMPLETED':
                    splInfo[0] = 'COMPLETED'
                    completed_jobs.append( job_name  )
                    if das_url != '':
                        das_urls[job_name] = das_url
                    info_content[i] = ';'.join(splInfo)

                elif status == 'RESUBMIT':
                    if int(splInfo[2]) > 5:
                        splInfo[0] = 'FAILED'
                        failed_jobs.append( job_name )
                        info_content[i] = ';'.join(splInfo)
                    else:
                        if RESUB:
                            resubmitJob( splInfo[1] )
                            splInfo[2] = str( int(splInfo[2]) +1 )
                            info_content[i] = ';'.join(splInfo)
                            print 'resubmitting failed jobs'

                elif status == 'PUBLICATE':
                    if int(splInfo[3]) > 5:
                        splInfo[0] = 'FAILED'
                        failed_jobs.append( job_name )
                        info_content[i] = ';'.join(splInfo)
                    else:
                        if RESUB:
                            resubmitPublication( splInfo[1] )
                            splInfo[3] = str( int(splInfo[3]) +1 )
                            info_content[i] = ';'.join(splInfo)
                            print 'publishing missing files'


        with open('das_urls.json','wb') as FSO:
            json.dump(das_urls, FSO,indent=4)
        
        with open('job_information.dat','w') as FSO:
            FSO.write('\n'.join(info_content))

        print '{0}\n{1}COMPLETED\n{0}\n{2}'.format('-'*80, ' '*25, '\n'.join(completed_jobs))
        print '{0}\n{1}FAILED\n{0}\n{2}'.format('-'*80, ' '*25, '\n'.join(failed_jobs))




def resubmitJob(path):
            proc = Popen('crab resubmit {0}'.format( path ),stdout = PIPE, shell=True)
            (out, err) = proc.communicate()

def resubmitPublication(path):
            proc = Popen('crab resubmit {0} --publication'.format( path ),stdout = PIPE, shell=True)
            (out, err) = proc.communicate()

def getStatus(path):

    proc = Popen('crab status {0}'.format( path ),stdout = PIPE, shell=True)
    (out, err) = proc.communicate()
    print '{0}\n{1}'.format('-'*80, path.split('/')[-1].replace('crab_','') )
    JOBS = False
    PUBL = False
    JFAIL = False
    PFAIL = False
    JCOMP = False
    das_url = ''

    for line in out.split('\n'):
        
        if 'DAS URL' in line:
            das_url = line.replace('%2F','/').split('input=')[1].split('&instance')[0]
            
        if 'Task status' in line:
            print line
            if 'COMPLETED' in line:
                JCOMP = True
             
        if 'Jobs status:' in line:
            JOBS = True
            
        if 'Publication status:' in line:
            JOBS = False
            PUBL = True

        if line  == '':
            JOBS = False
            PUBL = False

        if JOBS:
            print line
            if 'failed' in line:
                JFAIL = True

        if PUBL:
            print line
            if 'failed' in line:
                PFAIL = True

    if JCOMP:
      return 'COMPLETED', das_url
    elif JFAIL:
      return 'RESUBMIT', das_url
    elif PFAIL:
      return 'PUBLICATE', das_url
    else:
      return '', das_url



if __name__ == '__main__':
    user = os.environ['USER']

    
    paths =['{0}/src/CMGTools/H2TauTau/prod/MCSpring16/crab_MCSpring16'.format(os.environ['CMSSW_BASE']),
            '{0}/src/CMGTools/H2TauTau/prod/MCSpring16/crab_MCSpring16_reHLT'.format(os.environ['CMSSW_BASE']),
            '{0}/src/CMGTools/H2TauTau/prod/DATA/crab_DATA'.format(os.environ['CMSSW_BASE']),
            '{0}/src/CMGTools/TTHAnalysis/cfg/crab_HEPHY/crab_MCSpring16'.format(os.environ['CMSSW_BASE']),
            '{0}/src/CMGTools/TTHAnalysis/cfg/crab_HEPHY/crab_DATA16B'.format(os.environ['CMSSW_BASE']),
            #'{0}/src/CMGTools/TTHAnalysis/cfg/crab_HEPHY/crab_MCSpring16_reHLT'.format(os.environ['CMSSW_BASE'])
           ]

    parser = argparse.ArgumentParser()
    parser.add_argument('-ptime', help='Time between two status checks.', type=int, metavar = 'INT',default=3000)
    parser.add_argument('-nrep', help='Number of status checks.', type=int, metavar = 'INT',default=1)
    parser.add_argument('-res', help='Resubmit failed job?', action='store_true')

    args = vars(parser.parse_args())


    ptime = args.get('ptime',3000)
    nrep = args.get('nrep',1)
    res = args.get('res',False)
    for i in xrange(nrep):
        updateInformationFile(paths, RESUB=res)
        if nrep > 1 and i != nrep-1:
            time.sleep(ptime)
