import PhysicsTools.HeppyCore.framework.config as cfg
import os


#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()




SUSYGluGlu_mt_160203 = kreator.makeComponentHEPHY("SUSYGluGlu_mt_160203","/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-SUSYGluGlu_Fall2015_mt_newGT-f501ce246bdf6b2bc4e4d7be0312f2fa/USER","PRIVATE","*.root","phys03",1.0)

SUSYGluGlu_et_160203 = kreator.makeComponentHEPHY("SUSYGluGlu_et_160203","/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-SUSYGluGlu_Fall2015_et_newGT_160203-fcd7358c8ac03d2391eda9f4e6bf6bf2/USER","PRIVATE","*.root","phys03",1.0)


