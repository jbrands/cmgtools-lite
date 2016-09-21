import PhysicsTools.HeppyCore.framework.config as cfg
import os
import json




#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

dataDir = "$CMSSW_BASE/src/CMGTools/RootTools/data"

#####################################################################################################
def getComponent(Datasets, name, readCache):
    return kreator.makeComponentHEPHY(name, Datasets[name], "PRIVATE", ".*root", "phys03",1.0, readCache= readCache)

def getDataComponent(Datasets, name, readCache, json):
    return kreator.makeDataComponentHEPHY(name, Datasets[name], "PRIVATE", ".*root", "phys03",
                                          readCache = readCache,
                                          json = json)
#####################################################################################################

user = os.environ['USER']
component_path = '/afs/hephy.at/work/{0}/{1}/CMSSW_8_0_11/src/CMGTools/HephyTools/das_urls.json'.format(user[0], user)

if os.path.isfile(component_path):
        with open(component_path,'rb') as FSO:
                Datasets = json.load(FSO)
else:
    raise Warning('File {0} not found!!!'.format(component_path) )
#####################################################################################################


if __name__ == '__main__':
    for key in Datasets.keys():
        getComponent(Datasets, key,False)
else:
#####################################################################################################    
    TT_powheg_MCSpring16_160919  = getComponent(Datasets,"TT_powheg_MCSpring16_160919",False)
    DYJetsToLL_M_50_madgraphMLM_MCSpring16_160919 = getComponent(Datasets,"DYJetsToLL_M_50_madgraphMLM_MCSpring16_160919",False)
    DY1JetsToLL_M_50_madgraphMLM_MCSpring16_160919 = getComponent(Datasets,"DY1JetsToLL_M_50_madgraphMLM_MCSpring16_160919",False)
    DY2JetsToLL_M_50_madgraphMLM_MCSpring16_160919 = getComponent(Datasets,"DY2JetsToLL_M_50_madgraphMLM_MCSpring16_160919",False)
    DY3JetsToLL_M_50_madgraphMLM_MCSpring16_160919 = getComponent(Datasets,"DY3JetsToLL_M_50_madgraphMLM_MCSpring16_160919",False)
    # SUSYGluGluToHToTauTau_M_160_pythia8_MCSpring16_reHLT_160826 = getComponent(Datasets,"SUSYGluGluToHToTauTau_M_160_pythia8_MCSpring16_reHLT_160826",False)
    # SUSYGluGluToHToTauTau_M_160_pythia8_MCSpring16_160622 = getComponent(Datasets,"SUSYGluGluToHToTauTau_M_160_pythia8_MCSpring16_160622",True)
    # W4JetsToLNu_madgraphMLM_MCSpring16_160630 = getComponent(Datasets, "W4JetsToLNu_madgraphMLM_MCSpring16_160630",True)
    # W3JetsToLNu_madgraphMLM_MCSpring16_160630 = getComponent(Datasets, "W3JetsToLNu_madgraphMLM_MCSpring16_160630",True)
    # W2JetsToLNu_madgraphMLM_MCSpring16_160630 = getComponent(Datasets, "W2JetsToLNu_madgraphMLM_MCSpring16_160630",True)        
    # W1JetsToLNu_madgraphMLM_MCSpring16_160630 = getComponent(Datasets, "W1JetsToLNu_madgraphMLM_MCSpring16_160630",True)         
    # TT_powheg_MCSpring16_160630 = getComponent(Datasets, "TT_powheg_MCSpring16_160630",True)       
    # DYJetsToLL_M_50_madgraphMLM_MCSpring16_160630 = getComponent(Datasets, "DYJetsToLL_M_50_madgraphMLM_MCSpring16_160630",True)
    # VBFHToTauTau_M125_powheg_MCSpring16_160708 = getComponent(Datasets, "VBFHToTauTau_M125_powheg_MCSpring16_160708",True)
    # GluGluHToTauTau_M125_powheg_MCSpring16_160708 = getComponent(Datasets,"GluGluHToTauTau_M125_powheg_MCSpring16_160708",True)
    # VBFHToTauTau_M125_powheg_MCSpring16_reHLT_160727 = getComponent(Datasets,"VBFHToTauTau_M125_powheg_MCSpring16_reHLT_160727",True)
    # GluGluHToTauTau_M125_powheg_MCSpring16_reHLT_160727 = getComponent(Datasets,"GluGluHToTauTau_M125_powheg_MCSpring16_reHLT_160727",True)
    # SUSYGluGluToHToTauTau_M_160_pythia8_MCSpring16_160822 = getComponent(Datasets,"SUSYGluGluToHToTauTau_M_160_pythia8_MCSpring16_160822",True)
    # SingleMuonRun2016B_PromptReco_v2MINIAOD_DATA_160720 = getDataComponent(Datasets, "SingleMuonRun2016B_PromptReco_v2MINIAOD_DATA_160720",True,"$CMSSW_BASE/src/CMGTools/RootTools/data/Cert_271036-276384_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt")
#####################################################################################################

    

