import FWCore.ParameterSet.Config as cms

from CMGTools.Production.datasetToSource import datasetToSource
from CMGTools.H2TauTau.tools.setupJSON import setupJSON
# from CMGTools.H2TauTau.tools.setupRecoilCorrection import setupRecoilCorrection
from CMGTools.H2TauTau.tools.setupEmbedding import setupEmbedding
from CMGTools.H2TauTau.objects.jetreco_cff import addAK4Jets
from CMGTools.H2TauTau.tools.setupOutput import addTauMuOutput, addTauEleOutput, addDiTauOutput, addMuEleOutput, addDiMuOutput

sep_line = '-'*70

process = cms.Process("H2TAUTAU")

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(200))

numberOfFilesToProcess = -1
debugEventContent = False

# choose from 'tau-mu' 'di-tau' 'tau-ele' 'mu-ele' 'all-separate', 'all'
# channel = 'all'
channel = 'tau-mu'

# runSVFit enables the svfit mass reconstruction used for the H->tau tau analysis.
# if false, no mass calculation is carried out
runSVFit = False
# decide whether tau energy resolution has to enter SVfit integration
p4TransferFunctionFile = 'CMGTools/SVfitStandalone/data/svFitVisMassAndPtResolutionPDF.root' # Christians's default. If not touched, it would default to this anyways
integrateOverP4 = False # Default False

# increase to 1000 before running on the batch, to reduce size of log files
# on your account
reportInterval = 100

print sep_line
print 'channel', channel
print 'runSVFit', runSVFit

# Input & JSON             -------------------------------------------------

dataset_user = 'CMS'
dataset_name = ' /SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
dataset_files = '.*root'

#process.source = datasetToSource(
#    dataset_user,
#    dataset_name,
#    dataset_files,
#    )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("file:localTestFile.root")
#                            fileNames = cms.untracked.vstring("file:/data/jbrandstetter/CMGTools/tesFiles/WJets_miniAODv2.root") 
)                                                                                                                                                                                                           

process.source.inputCommands=cms.untracked.vstring(
    'keep *',
)



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

if numberOfFilesToProcess > 0:
    process.source.fileNames = process.source.fileNames[:numberOfFilesToProcess]

runOnMC = process.source.fileNames[0].find('Run201') == -1 and process.source.fileNames[0].find('embedded') == -1

if runOnMC == False:
    json = setupJSON(process)


# load the channel paths -------------------------------------------
process.load('CMGTools.H2TauTau.h2TauTau_cff')

# JAN: recoil correction disabled for now; reactivate if necessary
# setting up the recoil correction according to the input file
# recoilEnabled = False
# setupRecoilCorrection( process, runOnMC,
#                        enable=recoilEnabled, is53X=isNewerThan('CMSSW_5_2_X'))

isEmbedded = setupEmbedding(process, channel)
addAK4 = True
addPuppi = False

# Adding jet collection
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_v12'
# process.GlobalTag.globaltag = 'auto:run2_mc'


process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load('TrackingTools.TransientTrack.TransientTrackBuilder_cfi')
process.load('RecoBTag.Configuration.RecoBTag_cff')

if addAK4:
    addAK4Jets(process)
    process.mvaMetInputPath.insert(0, process.jetSequenceAK4)

if addPuppi:
    process.load('CommonTools/PileupAlgos/Puppi_cff')

    process.puppi.candName = cms.InputTag('packedPFCandidates')
    process.puppi.vertexName = cms.InputTag('offlineSlimmedPrimaryVertices')

    process.packedPFCandidatesWoMuon = cms.EDFilter("CandPtrSelector", src=cms.InputTag("packedPFCandidates"), cut=cms.string("fromPV>=2 && abs(pdgId)!=13 "))
    process.particleFlowNoMuonPUPPI = process.puppi.clone()
    process.particleFlowNoMuonPUPPI.candName = 'packedPFCandidatesWoMuon'

    from RecoMET.METProducers.PFMET_cfi import pfMet
    process.pfMetPuppi = pfMet.clone()
    process.pfMetPuppi.src = cms.InputTag('puppi')

    process.puppiPath = cms.Path(
        process.puppi +
        process.packedPFCandidatesWoMuon +
        process.particleFlowNoMuonPUPPI +
        process.pfMetPuppi
    )

# if '25ns' in process.source.fileNames[0] or 'mcRun2_asymptotic_v2' in process.source.fileNames[0]:
print 'Using 25 ns MVA MET training'
for mvaMETCfg in [process.mvaMETTauMu, process.mvaMETTauEle, process.mvaMETDiMu, process.mvaMETDiTau, process.mvaMETMuEle]:
    mvaMETCfg.inputFileNames = cms.PSet(
    U     = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru_7_4_X_miniAOD_25NS_July2015.root'),
    DPhi  = cms.FileInPath('RecoMET/METPUSubtraction/data/gbrphi_7_4_X_miniAOD_25NS_July2015.root'),
    CovU1 = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru1cov_7_4_X_miniAOD_25NS_July2015.root'),
    CovU2 = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru2cov_7_4_X_miniAOD_25NS_July2015.root')
    )
#     # process.mvaMETTauMu.inputRecords = cms.PSet(
#     #     U = cms.string("U1Correction"),
#     #     DPhi = cms.string("PhiCorrection"),
#     #     CovU1 = cms.string("CovU1"),
#     #     CovU2 = cms.string("CovU2")
#     # )
#     # process.mvaMETTauMu.inputFileNames = cms.PSet(
#     #     U     = cms.FileInPath('RecoMET/METPUSubtraction/data/gbrmet_53_Sep2013_type1.root'),
#     #     DPhi  = cms.FileInPath('RecoMET/METPUSubtraction/data/gbrmetphi_53_June2013_type1.root'),
#     #     CovU1 = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru1cov_53_Dec2012.root'),
#     #     CovU2 = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru2cov_53_Dec2012.root')
#     # )


# OUTPUT definition ----------------------------------------------------------
process.outpath = cms.EndPath()

# JAN: In 2015, we should finally make sure that we apply the correction to all
# generator-matched taus, regardless of the process

# 2012: don't apply Tau ES corrections for data (but do for embedded) or
# processes not containing real taus

# signalTauProcess = (process.source.fileNames[0].find('HToTauTau') != -1) or (process.source.fileNames[0].find('DY') != -1) or isEmbedded

if channel == 'all' or channel == 'all-separate':
    process.schedule = cms.Schedule(
        process.mvaMetInputPath,
        process.tauMuPath,
        process.tauElePath,
        process.muElePath,
        process.diTauPath,
        process.outpath
    )
elif channel == 'tau-mu':
    process.schedule = cms.Schedule(
        process.mvaMetInputPath,
        process.tauMuPath,
        process.outpath
    )
elif channel == 'tau-ele':
    process.schedule = cms.Schedule(
        process.mvaMetInputPath,
        process.tauElePath,
        process.outpath
    )
elif channel == 'di-tau':
    process.schedule = cms.Schedule(
        process.mvaMetInputPath,
        process.diTauPath,
        process.outpath
    )
elif channel == 'mu-ele':
    process.schedule = cms.Schedule(
        process.mvaMetInputPath,
        process.muElePath,
        process.outpath
    )
elif channel == 'di-mu':
    process.schedule = cms.Schedule(
        process.mvaMetInputPath,
        process.diMuPath,
        process.outpath
    )
else:
    raise ValueError('unrecognized channel')


if runOnMC:    
    process.genEvtWeightsCounterPath = cms.Path(process.genEvtWeightsCounter)
    process.schedule.insert(0, process.genEvtWeightsCounterPath)


if addPuppi:
    process.schedule.insert(-1, process.puppiPath)

# Enable printouts like this:
# process.cmgTauMuCorSVFitPreSel.verbose = True

if channel == 'tau-mu' or 'all' in channel:
    addTauMuOutput(process, debugEventContent, addPreSel=False, oneFile=(channel == 'all'))
if channel == 'tau-ele' or 'all' in channel:
    addTauEleOutput(process, debugEventContent, addPreSel=False, oneFile=(channel == 'all'))
if channel == 'mu-ele' or 'all' in channel:
    addMuEleOutput(process, debugEventContent, addPreSel=False, oneFile=(channel == 'all'))
if channel == 'di-mu' or 'all' in channel:
    addDiMuOutput(process, debugEventContent, addPreSel=False, oneFile=(channel == 'all'))
if channel == 'di-tau' or 'all' in channel:
    addDiTauOutput(process, debugEventContent, addPreSel=False, oneFile=(channel == 'all'))

# Message logger setup.
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = reportInterval
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(False))

if runSVFit:
    process.cmgTauMuCorSVFitPreSel.SVFitVersion = 2
    process.cmgTauEleCorSVFitPreSel.SVFitVersion = 2
    process.cmgDiTauCorSVFitPreSel.SVFitVersion = 2
    process.cmgMuEleCorSVFitPreSel.SVFitVersion = 2
else:
    process.cmgTauMuCorSVFitPreSel.SVFitVersion = 0
    process.cmgTauEleCorSVFitPreSel.SVFitVersion = 0
    process.cmgDiTauCorSVFitPreSel.SVFitVersion = 0
    process.cmgMuEleCorSVFitPreSel.SVFitVersion = 0

if integrateOverP4:
    process.cmgTauMuCorSVFitPreSel.integrateOverP4  = integrateOverP4
    process.cmgTauEleCorSVFitPreSel.integrateOverP4 = integrateOverP4
    process.cmgDiTauCorSVFitPreSel.integrateOverP4  = integrateOverP4
    process.cmgMuEleCorSVFitPreSel.integrateOverP4  = integrateOverP4

if p4TransferFunctionFile:
    process.cmgTauMuCorSVFitPreSel.p4TransferFunctionFile  = p4TransferFunctionFile
    process.cmgTauEleCorSVFitPreSel.p4TransferFunctionFile = p4TransferFunctionFile
    process.cmgDiTauCorSVFitPreSel.p4TransferFunctionFile  = p4TransferFunctionFile
    process.cmgMuEleCorSVFitPreSel.p4TransferFunctionFile  = p4TransferFunctionFile

print sep_line
print 'INPUT:'
print sep_line
print process.source.fileNames
print
if not runOnMC:
    print 'json:', json
print
print sep_line
print 'PROCESSING'
print sep_line
print 'runOnMC:', runOnMC
print
