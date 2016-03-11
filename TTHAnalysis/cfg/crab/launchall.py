import imp, os

# datasets to run as defined from run_susyMT2.cfg
# number of jobs to run per dataset decided based on splitFactor and fineSplitFactor from cfg file
# in principle one only needs to modify the following two lines:
#production_label = 'DATA_76X_16Dec_newTauIso'
production_label = 'MC_76X_fall2015_newMVAMet'
cmg_version = 'CMSSW_7_6_3'
storageSite = "T2_AT_Vienna"

debug  = False
useAAA = True

import sys
sys.path.append(os.environ['CMSSW_BASE']+'/src/CMGTools/RootTools/python/samples/')
from TEMPLATE_run_vienna_h2tau_cfg_crabTest import* 
#handle = open("heppy_config.py", 'r')
#cfo = imp.load_source("heppy_config", "heppy_config.py", handle)
#conf = cfo.config
#handle.close()

#os.system("scramv1 runtime -sh")
os.system("source /cvmfs/cms.cern.ch/crab3/crab.sh")

os.environ["PROD_LABEL"]  = production_label
os.environ["CMG_VERSION"] = cmg_version
os.environ["DEBUG"]       = str(debug)
os.environ["USEAAA"]      = str(useAAA)

from PhysicsTools.HeppyCore.framework.heppy_loop import split
for comp in config.components:
    # get splitting from config file according to splitFactor and fineSplitFactor (priority given to the latter)
    NJOBS = len(split([comp]))
    os.environ["NJOBS"] = str(NJOBS)
    os.environ["DATASET"] = str(comp.name)
    os.system("crab submit -c heppy_crab_config_env.py --wait")

os.system("rm -f python.tar.gz")
os.system("rm -f cmgdataset.tar.gz")
os.system("rm -f cafpython.tar.gz")
