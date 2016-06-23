import os
import time
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-run', help='Run N jobs', type=int, metavar = 'N',default=1)

args = vars(parser.parse_args())

if args.has_key('run'):
    nJobs = args.get('run',1)


for i in xrange(nJobs):

	ret_val = os.system('crab submit -c crabConf.py')
	if ret_val != 0:
		print 'Problem with calling. Probably no more open jobs'
		sys.exit()
	time.sleep(15)

print 'Submitted %d jobs' %nJobs

