import PhysicsTools.HeppyCore.framework.config as cfg
import os


#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

dataDir = "$CMSSW_BASE/src/CMGTools/RootTools/data"

#####################################################################################################
def getComponent(Datasets, name, readCache):
    return kreator.makeComponentHEPHY(name, Datasets[name], "PRIVATE", ".*root", "phys03",1.0, readCache)
#####################################################################################################

Datasets = {"test_CMG":
            "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/mspanrin-Test-7914e72860d9d2c46b1f45831813f869/USER",
            
            "SUSYGluGluToHToTauTau_MCSpring16_pythia8_160621":
            "/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/mspanrin-SUSYGluGluToHToTauTau_MCSpring16_pythia8_160621-7914e72860d9d2c46b1f45831813f869/USER"
           }
#####################################################################################################


if __name__ == '__main__':
    for key in Datasets.keys():
        getComponent(Datasets, key,False)
else:
#####################################################################################################

#    test_CMG = getComponent(Datasets, 'test_CMG',True)
    SUSYGluGluToHToTauTau_MCSpring16_pythia8_160621 = getComponent(Datasets,"SUSYGluGluToHToTauTau_MCSpring16_pythia8_160621",True)

#####################################################################################################

    
