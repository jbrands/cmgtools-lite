import PhysicsTools.HeppyCore.framework.config as cfg
import os


#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

dataDir = "$CMSSW_BASE/src/CMGTools/RootTools/data"

#####################################################################################################

SUSYGluGlu_mva_160312 = kreator.makeComponentHEPHY("SUSYGluGlu_mva_160312","/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-SUSYGluGlu_Fall2015_newMVAMET_160312-3ccb95530371a15c5bba8644a60df209/USER","PRIVATE","*.root","phys03",1.0)

#SUSYGluGlu_mt_160210 = kreator.makeComponentHEPHY("SUSYGluGlu_mt_160210","/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-SUSYGluGlu_Fall2015_newMVAMET_160310-87fe5eef8f7ead801c3114e6f087cc50/USER","PRIVATE","*.root","phys03",1.0)

#SUSYGluGlu_et_160203 = kreator.makeComponentHEPHY("SUSYGluGlu_et_160203","/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-SUSYGluGlu_Fall2015_et_newGT_160203-fcd7358c8ac03d2391eda9f4e6bf6bf2/USER","PRIVATE","*.root","phys03",1.0)


#####################################################################################################
#SingleMuon_16Dec_160219 = kreator.makeDataComponentHEPHY("SingleMuon_16Dec_160219","/SingleMuon/jbrandst-Data2015_16Dec_mt_160210-4850eb715c4e66bb333b420567db4539/USER", "PRIVATE", "*.root","phys03","$CMSSW_BASE/src/CMGTools/RootTools/data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt")

#SingleElectron_16Dec_160226 = kreator.makeDataComponentHEPHY("SingleElectron_16Dec_160226","/SingleElectron/jbrandst-Data2015_16Dec_et_160224-2d90d1cf4fc758c480cd278a993cb33c/USER", "PRIVATE", "*.root","phys03","$CMSSW_BASE/src/CMGTools/RootTools/data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt")


#####################################################################################################

#TT_Fall2015_mt_160208 = kreator.makeComponentHEPHY("TT_Fall2015_mt_160208","/TT_TuneCUETP8M1_13TeV-powheg-pythia8/jbrandst-TT_TuneCUETP8M1_Fall2015_mt_160208-f501ce246bdf6b2bc4e4d7be0312f2fa/USER","PRIVATE","*.root","phys03",1.0)

#DYJets_Fall2015_newMVAMet_160311 = kreator.makeComponentHEPHY("DYJets_Fall15_newMVAMet_160311","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/jbrandst-DYJetsToLL_MCFall15_160310-87fe5eef8f7ead801c3114e6f087cc50/USER","PRIVATE","*.root","phys03",1.0) 

#DYJets_Fall2015_mt_160220_wo1step = kreator.makeMCComponent("DYJets_Fall2015_mt_160220_wo1step","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM","CMS",".*root",1.0)

#DYJets_Fall2015_mt_amcatnloFXFX_160223_wo1step = kreator.makeMCComponent("DYJets_Fall2015_mt_amcatnloFXFX_160223_wo1step","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM","CMS",".*root",1.0)

#WJetsToLNu_Fall2015_mt_160210 = kreator.makeComponentHEPHY("WJetsToLNu_Fall2015_mt_160208","/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/jbrandst-WJetsToLNu_Fall2015_mt_160210_2-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#W1JetsToLNu_Fall2015_mt_160210 = kreator.makeComponentHEPHY("W1JetsToLNu_Fall2015_mt_160208","/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/jbrandst-WJetsToLNu_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#####################################################################################################

#ST_tchannel_antitop_4f_Fall2015_mt_160218 = kreator.makeComponentHEPHY("ST_tchannel_antitop_4f_Fall2015_mt_160218","/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/jbrandst-ST_t-channel_antitop_4f_leptonDecays_powheg_mt_160216-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#ST_tchannel_top_4f_Fall2015_mt_160218 = kreator.makeComponentHEPHY("ST_tchannel_top_4f_Fall2015_mt_160218","/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/jbrandst-ST_t-channel_top_4f_leptonDecays_powheg_mt_160216-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#ST_tW_antitop_5f_Fall2015_mt_160218 = kreator.makeComponentHEPHY("ST_tW_antitop_5f_Fall2015_mt_160218","/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/jbrandst-ST_tW_antitop_5f_inclusiveDecays_powheg_mt_160216-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#ST_tW_top_5f_Fall2015_mt_160218 = kreator.makeComponentHEPHY("ST_tW_top_5f_Fall2015_mt_160218","/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/jbrandst-ST_tW_top_5f_inclusiveDecays_powheg_mt_160216-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)


#####################################################################################################

#QCD_Pt20to30_MuEnrichedPt5 = kreator.makeComponentHEPHY("QCD_Pt20to30_MuEnrichedPt5","/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/jbrandst-QCD_Pt-20to30_MuEnrichedPt15_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#QCD_Pt30to50_MuEnrichedPt5 = kreator.makeComponentHEPHY("QCD_Pt30to50_MuEnrichedPt5","/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/jbrandst-QCD_Pt-30to50_MuEnrichedPt15_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#QCD_Pt50to80_MuEnrichedPt5 = kreator.makeComponentHEPHY("QCD_Pt50to80_MuEnrichedPt5","/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/jbrandst-QCD_Pt-50to80_MuEnrichedPt15_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#QCD_Pt80to120_MuEnrichedPt5 = kreator.makeComponentHEPHY("QCD_Pt80to120_MuEnrichedPt5","/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/jbrandst-QCD_Pt-80to120_MuEnrichedPt15_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#QCD_Pt120to170_MuEnrichedPt5 = kreator.makeComponentHEPHY("QCD_Pt120to170_MuEnrichedPt5","/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/jbrandst-QCD_Pt-120to170_MuEnrichedPt15_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#QCD_Pt170to300_MuEnrichedPt5 = kreator.makeComponentHEPHY("QCD_Pt170to300_MuEnrichedPt5","/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/jbrandst-QCD_Pt-170to300_MuEnrichedPt15_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#QCD_Pt300to470_MuEnrichedPt5 = kreator.makeComponentHEPHY("QCD_Pt300to470_MuEnrichedPt5","/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/jbrandst-QCD_Pt-300to470_MuEnrichedPt15_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)

#QCD_Pt20toInf_MuEnrichedPt15 = kreator.makeComponentHEPHY("QCD_Pt20toInf_MuEnrichedPt15","/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/jbrandst-QCD_Pt-20toInf_MuEnrichedPt15_Fall2015_mt_160210-1960a87552f63b63e646807fa2728c2b/USER","PRIVATE","*.root","phys03",1.0)
