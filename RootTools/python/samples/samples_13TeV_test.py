import PhysicsTools.HeppyCore.framework.config as cfg
import os


#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()




TT_powheg = kreator.makeComponentHEPHY("TT_powheg_151209_tauEle","/TT_TuneCUETP8M1_13TeV-powheg-pythia8/mflechl-ttbar_ele_MC1_151209-71a3c028dfed4d1fdaf7c36c202a6c4a/USER","PRIVATE","*.root","phys03",1.0)


