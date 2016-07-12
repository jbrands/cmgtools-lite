##########################################################
##       CONFIGURATION FOR Higgs->tautau TREES          ##
## skim condition: >= 0 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg


#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.higgsCore_modules_cff import * 

# Redefine what I need
lepAna.loose_muon_relIso = 999 #reliso03
lepAna.mu_isoCorr = "deltaBeta" 

lepAna.loose_electron_relIso = 999 #reliso03 
lepAna.ele_isoCorr = "deltaBeta" 

tauAna.tauLooseID = "decayModeFindingNewDMs"
tauAna.tauID = "decayModeFindingNewDMs"
tauAna.vetoLeptons = False
tauAna.vetoLeptonsPOG = False
tauAna.ptMin = 20
tauAna.etaMax = 2.5


jetAna.minLepPt = 10
jetAna.jetPt = 20
jetAna.jetEta = 4.7

jetAna.mcGT     = "Spring16_25nsV3_MC"
jetAna.dataGT   = "Fall15_25nsV2_MC"
jetAna.do_mc_match = True
jetAna.smearJets = False #should be false in susycore, already                                      
jetAna.calculateSeparateCorrections = True 
jetAna.recalibrateJets =  True #For data  
jetAna.applyJetSmearing = False                                                                                                                                                        

metAna.recalibrate = False #should be false in susycore, already 
metAna.isDilepton=True
metAna.isTauMu=True
metAna.isTauEle=False

# --- LEPTON SKIMMING ---
#ttHLepSkim.minLeptons = 0
#ttHLepSkim.maxLeptons = 999
##LepSkim.idCut  = ""
##LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---

#ttHReclusterJets = cfg.Analyzer(
#            'ttHReclusterJetsAnalyzer',
#            )


## isoTrackAna.setOff=False

#from CMGTools.TTHAnalysis.analyzers.ttHReclusterJetsAnalyzer  import ttHReclusterJetsAnalyzer
#ttHReclusterJets = cfg.Analyzer(
#    ttHReclusterJetsAnalyzer, name="ttHReclusterJetsAnalyzer",
#    )
from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## Insert the SV analyzer in the sequence
#higgsCoreSequence.insert(higgsCoreSequence.index(ttHCoreEventAna),
#                        ttHFatJetAna)
#higgsCoreSequence.insert(higgsCoreSequence.index(ttHCoreEventAna),
#                        ttHSVAna)
#higgsCoreSequence.insert(higgsCoreSequence.index(ttHCoreEventAna),
#                        ttHHeavyFlavourHadronAna)



#from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14  import *
#from CMGTools.RootTools.samples.samples_13TeV_74X_privat  import *

triggerFlagsAna.triggerBits = {

 'IsoMu18'                                              : ['HLT_IsoMu18_v3'],
 'IsoMu20'                                              : ['HLT_IsoMu20_v4'],
 'IsoMu22'                                              : ['HLT_IsoMu22_v3'],
 'IsoMu22_eta2p'                                        : ['HLT_IsoMu22_eta2p1_v2'],
 'IsoMu24'                                              : ['HLT_IsoMu24_v2'],
 'IsoMu27'                                              : ['HLT_IsoMu27_v4'],
 'IsoTkMu18'                                            : ['HLT_IsoTkMu18_v3'],
 'IsoTkMu20'                                            : ['HLT_IsoTkMu20_v5'],
 'IsoTkMu22'                                            : ['HLT_IsoTkMu22_v3'],
 'IsoTkMu22_eta2p'                                      : ['HLT_IsoTkMu22_eta2p1_v2'],
 'IsoTkMu24'                                            : ['HLT_IsoTkMu24_v2'],
 'IsoTkMu27'                                            : ['HLT_IsoTkMu27_v4'],
 'IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1'              : ['HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v5'],
 'IsoMu17_eta2p1_LooseIsoPFTau2'                        : ['HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v5'],
 'IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1'              : ['HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v2'],
 'IsoMu19_eta2p1_LooseIsoPFTau2'                        : ['HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v2'],
 'IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1'              : ['HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v2'],
 'Ele23_WPLoose_Gsf'                                    : ['HLT_Ele23_WPLoose_Gsf_v4'],
 'Ele24_eta2p1_WPLoose_Gsf'                             : ['HLT_Ele24_eta2p1_WPLoose_Gsf_v2'],
 'Ele25_WPTight_Gsf'                                    : ['HLT_Ele25_WPTight_Gsf_v2'],
 'Ele25_eta2p1_WPLoose_Gsf'                             : ['HLT_Ele25_eta2p1_WPLoose_Gsf_v2'],
 'Ele25_eta2p1_WPTight_Gsf'                             : ['HLT_Ele25_eta2p1_WPTight_Gsf_v2'],
 'Ele27_WPLoose_Gsf'                                    : ['HLT_Ele27_WPLoose_Gsf_v2'],
 'Ele27_WPTight_Gsf'                                    : ['HLT_Ele27_WPTight_Gsf_v2'],
 'Ele27_eta2p1_WPLoose_Gsf'                             : ['HLT_Ele27_eta2p1_WPLoose_Gsf_v3'],
 'Ele27_eta2p1_WPTight_Gsf'                             : ['HLT_Ele27_eta2p1_WPTight_Gsf_v3'],
 'Ele32_eta2p1_WPTight_Gsf'                             : ['HLT_Ele32_eta2p1_WPTight_Gsf_v3'],
 'Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : ['HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v3'],
 'Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : ['HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2'],
 'Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20'             : ['HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v2'],
 'Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : ['HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2'],
 'Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1'    : ['HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2']

}

triggerObjsAna.triggers = {
    'HLT_IsoMu18_v3',
    'HLT_IsoMu20_v4',
    'HLT_IsoMu22_v3',
    'HLT_IsoMu22_eta2p1_v2',
    'HLT_IsoMu24_v2',
    'HLT_IsoMu27_v4',
    'HLT_IsoTkMu18_v3',
    'HLT_IsoTkMu20_v5',
    'HLT_IsoTkMu22_v3',
    'HLT_IsoTkMu22_eta2p1_v2',
    'HLT_IsoTkMu24_v2',
    'HLT_IsoTkMu27_v4',
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v5',
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v5',
    'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v2',
    'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v2',
    'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v2',
    'HLT_Ele23_WPLoose_Gsf_v4',
    'HLT_Ele24_eta2p1_WPLoose_Gsf_v2',
    'HLT_Ele25_WPTight_Gsf_v2',
    'HLT_Ele25_eta2p1_WPLoose_Gsf_v2',
    'HLT_Ele25_eta2p1_WPTight_Gsf_v2',
    'HLT_Ele27_WPLoose_Gsf_v2',
    'HLT_Ele27_WPTight_Gsf_v2',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_v3',
    'HLT_Ele27_eta2p1_WPTight_Gsf_v3',
    'HLT_Ele32_eta2p1_WPTight_Gsf_v3',
    'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v3',
    'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2',
    'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v2',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2',
   #put trigger here for data                                                                         
}


# triggerFlagsAna.triggerBits = {
#     "Ele22_eta2p1_WP75_Gsf"                   : [ "HLT_Ele22_eta2p1_WP75_Gsf" ],
#     "Ele23_WPLoose_Gsf"                       : [ "HLT_Ele23_WPLoose_Gsf_v*" ],
#     "IsoMu17_eta2p1"                          : [ "HLT_IsoMu17_eta2p1" ],
#     "IsoMu18_v"                               : [ "HLT_IsoMu18_v" ],
#     "IsoMu17_eta2p1_LooseIsoPFTau20"          : [ "HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v*" ],
#     "IsoMu24_eta2p1"                          : [ "HLT_IsoMu24_eta2p1_v*" ],
#     "IsoMu20_eta2p1_IterTrk02"                : [ "HLT_IsoMu20_eta2p1_IterTrk02_v*" ],
#     "IsoTkMu20_eta2p1_IterTrk02"              : [ "HLT_IsoTkMu20_eta2p1_IterTrk02_v*" ],
#     "IsoMu24_IterTrk02"                       : [ "HLT_IsoMu24_IterTrk02_v*" ],
#     "IsoTkMu24_IterTrk02"                     : [ "HLT_IsoTkMu24_IterTrk02_v*" ],
#     "Ele32_eta2p1_WP75_Gsf"                   : [ "HLT_Ele32_eta2p1_WP75_Gsf_v*"],
#     "DoubleMediumIsoPFTau35_eta2p1"           : [ "HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v2"],
# #put trigger here for data                                                                            
# }

# triggerObjsAna.triggers = {
#    "HLT_IsoMu17_eta2p1_v1",
#    "HLT_IsoMu18_v2",
#    "HLT_IsoMu22_v1",
#    "HLT_IsoMu24_eta2p1_v2",
#    "HLT_Ele22_eta2p1_WP75_Gsf_v1",
#    "HLT_Ele23_WPLoose_Gsf_v3",
#    "HLT_Ele32_eta2p1_WP75_Gsf_v1",
#    "HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v2",
#    #put trigger here for data                                                                         
# }

# Tree Producer
from CMGTools.TTHAnalysis.analyzers.treeProducerHiggsToTauTau import *
## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerHiggsToTauTau',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     PDFGen = PDFGen,
     globalVariables = higgsToTauTau_globalVariables,
     globalObjects = higgsToTauTau_globalObjects,
     collections = higgsToTauTau_collections,
)



#-------- SAMPLES AND TRIGGERS -----------

#from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *

#from CMGTools.RootTools.samples.samples_13TeV_test import *
#print "Working"

#selectedComponents = [ SingleMu, DoubleElectron, TTHToWW_PUS14, DYJetsToLL_M50_PU20bx25, TTJets_PUS14 ]
#TTJets.splitFactor = 1000
#selectedComponents = [TTJets]

#selectedComponents = [QCD_HT_1000ToInf, QCD_HT_250To500, QCD_HT_500To1000, SMS_T1tttt_2J_mGl1200_mLSP800, SMS_T1tttt_2J_mGl1500_mLSP100, SMS_T2tt_2J_mStop425_mLSP325, SMS_T2tt_2J_mStop500_mLSP325, SMS_T2tt_2J_mStop650_mLSP325, SMS_T2tt_2J_mStop850_mLSP100, TBarToLeptons_sch, TBarToLeptons_tch, TBar_tWch, TTH, TTWJets, TTZJets, TToLeptons_sch, TToLeptons_tch, T_tWch]
#selectedComponents =WJetsToLNuHT +  [WJetsToLNu]  
##selectedComponents = DYJetsM50HT
##selectedComponents = MySamples 
#-------- SEQUENCE

#selectedComponents = HiggsSignalSamples

sequence = cfg.Sequence(
    higgsCoreSequence+[
#    ttHEventAna,
#    ttHReclusterJets,
    treeProducer,
    ])


#-------- HOW TO RUN
#test = 0
#selectedComponents = [ QCD_Pt_20toInf_MuEnriched15, QCD_Pt_20to30_MuEnrichedPt5, QCD_Pt_30to50_MuEnrichedPt5, QCD_Pt_50to80_MuEnrichedPt5, QCD_Pt_80to120_MuEnrichedPt5, QCD_Pt_120to170_MuEnrichedPt5, QCD_Pt_170to300_MuEnrichedPt5, QCD_Pt_300to470_MuEnrichedPt5 ]
#selectedComponents = [ TT_Fall2015_mt_160208 ]

#selectedComponents = [ DYJets_Fall2015_newMVAMet_160317 ]

selectedComponents = [ ]
#selectedComponents = [ DYJets_Fall2015_nlo_wo1step ]

#selectedComponents = [ DYJets_Fall2015_mt_amcatnloFXFX_160223_wo1step ]


# test = 3
# if test==1:
#     # test files XX-YY of first component                  
#     comp = XX_DSNAME_XX
#     comp.files = ['root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/jbrandst/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/SUSYGluGlu_miniAOD2_tauMu_151218/151218_143318/0000/tauMu_fullsel_tree_CMG_1.root']
#     print comp.files
#     selectedComponents = [comp]
#     comp.splitFactor = 250
#     comp.puFileData = 'MyDataPileupHistogram_observed_new.root'
#     comp.puFileMC = 'MyMCPileupHistogram_normOfficial.root'
# elif test==2:    
#     # test files XX-YY of first component                  
#     comp = SUSYGluGlu_mt_160203
#     comp.files = ['/data/jbrandstetter/CMGTools/76X/tauMu_fullsel_tree_CMG.root']
#     print comp.files
#     selectedComponents = [comp]
#     comp.splitFactor = 250
#     comp.puFileData = '../MyDataPileupHistogram_observed_new.root'
#     comp.puFileMC = '../MyMCPileupHistogram_normOfficial.root'
# elif test==3:
#     # test files XX-YY of first component
#     #comp = SUSYGluGlu_mt_160203
#     #comp = TT_Fall2015_mt_160208
#     for comp in selectedComponents:
#         comp.isMC=1
#         comp.isData=0
#         comp.splitFactor = 2500
#         comp.files = comp.files[:]
#         #selectedComponents = [comp]
#         comp.puFileData = "$CMSSW_BASE/src/CMGTools/RootTools/data/MyDataPileupHistogram_observed_new.root"
#         comp.puFileMC = "$CMSSW_BASE/src/CMGTools/RootTools/data/MyMCPileupHistogram_normOfficial.root"    

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     events_class = Events)
