#########################################################
##       CONFIGURATION FOR Higgs->tautau TREES          ##
## skim condition: >= 0 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

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
jetAna.dataGT   = "Fall15_25nsV2_DATA"
jetAna.do_mc_match = False                                    
jetAna.calculateSeparateCorrections = True 
jetAna.recalibrateJets =  True #For data  
jetAna.applyJetSmearing = False                                                                                                                                                        

metAna.recalibrate = False #should be false in susycore, already 
metAna.isDilepton=True
metAna.isTauMu=False
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
# from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
# ttHEventAna = cfg.Analyzer(
#     ttHLepEventAnalyzer,
#     name="ttHLepEventAnalyzer",
#     minJets25 = 0,
#     )

# Tree Producer
triggerFlagsAna.processName = 'HLT'
triggerFlagsAna.triggerBits = {

 "IsoMu18"                                              : [ ''.join(["HLT_IsoMu18_v",str(i)])  for i in xrange(1,5)],
 "IsoMu20"                                              : [ ''.join(["HLT_IsoMu20_v",str(i)])  for i in xrange(1,5)],
 "IsoMu22"                                              : [ ''.join(["HLT_IsoMu22_v",str(i)])  for i in xrange(1,5)],
 "IsoMu22_eta2p1"                                       : [ ''.join(["HLT_IsoMu22_eta2p1_v",str(i)])  for i in xrange(1,5)],
 "IsoMu24"                                              : [ ''.join(["HLT_IsoMu24_v",str(i)])  for i in xrange(1,5)],
 "IsoMu27"                                              : [ ''.join(["HLT_IsoMu27_v",str(i)])  for i in xrange(1,5)],
 "IsoTkMu18"                                            : [ ''.join(["HLT_IsoTkMu18_v",str(i)])  for i in xrange(1,5)],
 "IsoTkMu20"                                            : [ ''.join(["HLT_IsoTkMu20_v",str(i)])  for i in xrange(1,5)],
 "IsoTkMu22"                                            : [ ''.join(["HLT_IsoTkMu22_v",str(i)])  for i in xrange(1,5)],
 "IsoTkMu22_eta2p1"                                     : [ ''.join(["HLT_IsoTkMu22_eta2p1_v",str(i)])  for i in xrange(1,5)],
 "IsoTkMu24"                                            : [ ''.join(["HLT_IsoTkMu24_v",str(i)])  for i in xrange(1,5)],
 "IsoTkMu27"                                            : [ ''.join(["HLT_IsoTkMu27_v",str(i)])  for i in xrange(1,5)],
 "IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1"              : [ ''.join(["HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v",str(i)])  for i in xrange(1,5)],
 "IsoMu17_eta2p1_LooseIsoPFTau2"                        : [ ''.join(["HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v",str(i)])  for i in xrange(1,5)],
 "IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1"              : [ ''.join(["HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v",str(i)])  for i in xrange(1,5)],
 "IsoMu19_eta2p1_LooseIsoPFTau2"                        : [ ''.join(["HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v",str(i)])  for i in xrange(1,5)],
 "IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1"              : [ ''.join(["HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v",str(i)])  for i in xrange(1,5)],
 "Ele23_WPLoose_Gsf"                                    : [ ''.join(["HLT_Ele23_WPLoose_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele24_eta2p1_WPLoose_Gsf"                             : [ ''.join(["HLT_Ele24_eta2p1_WPLoose_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele25_WPTight_Gsf"                                    : [ ''.join(["HLT_Ele25_WPTight_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele25_eta2p1_WPLoose_Gsf"                             : [ ''.join(["HLT_Ele25_eta2p1_WPLoose_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele25_eta2p1_WPTight_Gsf"                             : [ ''.join(["HLT_Ele25_eta2p1_WPTight_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele27_WPLoose_Gsf"                                    : [ ''.join(["HLT_Ele27_WPLoose_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele27_WPTight_Gsf"                                    : [ ''.join(["HLT_Ele27_WPTight_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele27_eta2p1_WPLoose_Gsf"                             : [ ''.join(["HLT_Ele27_eta2p1_WPLoose_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele27_eta2p1_WPTight_Gsf"                             : [ ''.join(["HLT_Ele27_eta2p1_WPTight_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele32_eta2p1_WPTight_Gsf"                             : [ ''.join(["HLT_Ele32_eta2p1_WPTight_Gsf_v",str(i)])  for i in xrange(1,5)],
 "Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1"    : [ ''.join(["HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v",str(i)])  for i in xrange(1,5)],
 "Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1"    : [ ''.join(["HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v",str(i)])  for i in xrange(1,5)],
 "Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20"             : [ ''.join(["HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v",str(i)])  for i in xrange(1,5)],
 "Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1"    : [ ''.join(["HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v",str(i)])  for i in xrange(1,5)],
 "Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1"    : [ ''.join(["HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v",str(i)])  for i in xrange(1,5)]

}
triggerObjsAna.triggerResultsHandle = ('TriggerResults', '', 'HLT')

triggerObjsAna.extraTrig = triggerFlagsAna.triggerBits["IsoMu22"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoMu24"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoMu27"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoTkMu22"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoTkMu22_eta2p1"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoTkMu24"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoTkMu27"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoMu17_eta2p1_LooseIsoPFTau2"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoMu19_eta2p1_LooseIsoPFTau2"]
triggerObjsAna.extraTrig += triggerFlagsAna.triggerBits["IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1"]


jsonAna.json="$CMSSW_BASE/src/CMGTools/RootTools/data/Cert_271036-276384_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt"

from CMGTools.TTHAnalysis.analyzers.treeProducerHiggsToTauTau import *
## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer,
     name='treeProducerHiggsToTauTau',
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
#if getHeppyOption("loadSamples"):

#-------- SEQUENCE

#selectedComponents = HiggsSignalSamples

sequence = cfg.Sequence(
    higgsCoreSequence+[
#    ttHEventAna,
#    ttHReclusterJets,
    treeProducer,
    ])



selectedComponents = []   



#
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events

config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     events_class = Events)



