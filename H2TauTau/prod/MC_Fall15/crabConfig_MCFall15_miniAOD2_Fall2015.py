from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
#config.General.requestName   = 'DYJetsToLL_MCFall15_nlo_160318'
config.General.requestName   = 'DY1JetsToLL_MCFall15_160322'
#config.General.requestName   = 'DY2JetsToLL_MCFall15_160319'
#config.General.requestName   = 'DY3JetsToLL_MCFall15_160319'
#config.General.requestName   = 'DY4JetsToLL_MCFall15_160319'
#config.General.requestName   = 'TTbar_MCFall15_160319'
#config.General.requestName   = 'WJets_MCFall15_160319'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'runMVAMET.py'
config.JobType.inputFiles = ['Fall15_25nsV2_MC.db']

config.section_("Data")
#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
config.Data.inputDataset = '/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
#config.Data.inputDataset = '/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
#config.Data.inputDataset = '/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
#config.Data.inputDataset = '/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
#config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/MINIAODSIM'
#config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
#config.Data.publication = False
# This string is used to construct the output dataset name
#config.Data.outputDatasetTag = 'DYJetsToLL_MCFall15_nlo_160318'
config.Data.outputDatasetTag = 'DY1JetsToLL_MCFall15_160322'
#config.Data.outputDatasetTag = 'DY2JetsToLL_MCFall15_160319'
#config.Data.outputDatasetTag = 'DY3JetsToLL_MCFall15_160319'
#config.Data.outputDatasetTag = 'DY4JetsToLL_MCFall15_160319'
#config.Data.outputDatasetTag = 'TTbar_MCFall15_160319'
#config.Data.outputDatasetTag = 'WJets_MCFall15_160319'
#!!!
config.Data.ignoreLocality = True

# These values only make sense for processing data
#    Select input data based on a lumi mask
#config.Data.lumiMask = 'Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
#    Select input data based on run-ranges
#config.Data.runRange = '190456-194076'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ["T2_UK_SGrid_Bristol","T2_DE_DESY", "T2_US_Wisconsin"]
config.Site.whitelist = ["T2_AT_Vienna"]
#config.Site.blacklist = ['T2_US_Purdue', 'T2_BE_IIHE', 'T2_US_Wisconsin', 'T2_UK_SGrid_Bristol', 'T2_US_Nebraska']
