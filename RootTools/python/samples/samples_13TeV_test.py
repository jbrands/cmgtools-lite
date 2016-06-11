import PhysicsTools.HeppyCore.framework.config as cfg
import os


#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

dataDir = "$CMSSW_BASE/src/CMGTools/RootTools/data"

#####################################################################################################

test_CMG = kreator.makeComponentHEPHY("test","/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-SUSYGluGlu_Fall2015_newMVAMET_160318-1a223008585dcc4d5a49edc447ee1d23/USER","PRIVATE","*.root","phys03",1.0)

