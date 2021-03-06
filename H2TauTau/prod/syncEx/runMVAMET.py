import sys
from CMGTools.Production.datasetToSource import datasetToSource
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.tauTools import *
from CMGTools.H2TauTau.objects.ViennaCuts_cff import *
from RecoMET.METPUSubtraction.MVAMETConfiguration_cff import runMVAMET
#from CMGTools.diLeptonSelector.diLeptonFilter_cfi.py import

process = cms.Process("MVAMET")
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(200))
#process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))
numberOfFilesToProcess = -1

#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_RunIIFall15DR76_v1'
#process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_v12'

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')

#process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')
#process.load('TrackingTools.TransientTrack.TransientTrackBuilder_cfi')
#process.load('RecoBTag.Configuration.RecoBTag_cff')


dataset_user = 'CMS'
dataset_name = ' /SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
dataset_files = '.*root'

#process.source = datasetToSource(                                                                   
#    dataset_user,
#    dataset_name,
#    dataset_files,
#    )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("file:localTestFile_WJets.root")
#                            fileNames = cms.untracked.vstring("file:localTestFile.root")
#                            fileNames = cms.untracked.vstring("file:localTestFile_DY.root")
                            )


isData=False 

if not hasattr(process, "p"):                                                                                                                      
         process.p = cms.Path() 
#process.load('CMGTools.H2TauTau.objects.ViennaCuts_cff')
process.load('CMGTools.diLeptonSelector.diLeptonFilter_cfi')
process.eventDiLeptonFilter
#process.muonPreSelection
#process.electronPreSelection
process.p *= (process.eventDiLeptonFilter) 

from RecoMET.METPUSubtraction.localSqlite import loadLocalSqlite
loadLocalSqlite(process, "Fall15_25nsV2_MC.db") 

#if options.reapplyJEC:
from RecoMET.METPUSubtraction.localSqlite import recorrectJets
recorrectJets(process, isData)
jetCollection = "patJetsReapplyJEC"

# configure MVA MET
runMVAMET( process, jetCollectionPF = jetCollection)
process.MVAMET.srcLeptons  = cms.VInputTag("slimmedMuons", "slimmedElectrons", "slimmedTaus")
process.MVAMET.requireOS = cms.bool(False)

process.source.inputCommands = cms.untracked.vstring(
    'keep *'
)

process.options = cms.untracked.PSet(
    allowUnscheduled=cms.untracked.bool(True)
)

process.genEvtWeightsCounter = cms.EDProducer(
    'GenEvtWeightCounter',
    verbose = cms.untracked.bool(False)
)

if not isData:
    process.genEvtWeightsCounterPath = cms.Path(process.genEvtWeightsCounter)
    #process.schedule.insert(0, process.genEvtWeightsCounterPath)

if numberOfFilesToProcess > 0:
    process.source.fileNames = process.source.fileNames[:numberOfFilesToProcess]

## logger
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10

#! Output and Log                                                                                                                                      
from CMGTools.H2TauTau.eventContent.common_cff import common                      
process.output = cms.OutputModule("PoolOutputModule",
                                  fileName = cms.untracked.string('outfile_newMVA.root'),
                                  outputCommands = cms.untracked.vstring(common),
                                  SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring('p'))
                                  )
process.out = cms.EndPath(process.output)

#  LocalWords:  Outputcommands










# if options.saveMapForTraining:
#     if not hasattr(process, "p"):
#         process.p = cms.Path()
#     process.load('CommonTools.UtilAlgos.TFileService_cfi')
#     process.TFileService.fileName = cms.string('output.root')
#     process.TFileService.closeFileFast = cms.untracked.bool(True)
#     from RecoMET.METPUSubtraction.mapAnalyzer_cff import MAPAnalyzer
#     process.MAPAnalyzer = MAPAnalyzer
#     process.MVAMET.saveMap = cms.bool(True)
#     process.genZEvent = cms.EDFilter("GenParticleSelector",
#         filter = cms.bool(True),
#         src = cms.InputTag("prunedGenParticles"),
#         cut = cms.string('abs(pdgId()) == 13 && !isDirectPromptTauDecayProductFinalState()'),
#         #cut = cms.string('isDirectPromptTauDecayProductFinalState()'),                                                                                  
#         stableOnly = cms.bool(False)
#     )
#     process.skimmvamet = cms.Sequence( process.genZEvent * process.MVAMET * process.MAPAnalyzer)
#     process.p *= (process.skimmvamet)

# else:
#     process.output = cms.OutputModule("PoolOutputModule",
#                                       fileName = cms.untracked.string('output_particles.root'),
#                                       outputCommands = cms.untracked.vstring(
#                                                                              'keep patMETs_MVAMET_MVAMET_MVAMET',
#                                                                              'keep *_patJetsReapplyJEC_*_MVAMET'
#                                                                              ),
#                                       SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring('p'))
#                                       )
#     process.out = cms.EndPath(process.output)





