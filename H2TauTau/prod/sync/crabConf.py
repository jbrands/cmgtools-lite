from WMCore.Configuration import Configuration
################################################################################
class DatasetChooser():
    def __init__(self, datasets_path, pref_dataset = ''):
        
           
        self.datasets_path = datasets_path

    def timestamp(self, tag):
        from time import localtime
        if tag is '': return ''

        lt = localtime()
        y = str(lt.tm_year).replace('20','')
        m = str(lt.tm_mon) if lt.tm_mon>9 else '{0}{1}'.format('0',lt.tm_mon)
        d = str(lt.tm_mday) if lt.tm_mday>9 else '{0}{1}'.format('0',lt.tm_mday)

        return '%s_%s%s%s' % (tag, y,m,d)

    def GetOpenJob(self):
        from json import load, dump
        from os import environ
        from sys import exit

        with open(self.datasets_path ,'rb') as FSO:
            dsets=load(FSO)

        for sets in dsets:
            for el in dsets[sets]:
                if dsets[sets][el]['status'] == 'open':
                    self.strDatacard = dsets[sets][el]['datacard']
                    self.strTag = self.timestamp( '{0}_{1}'.format(el,
                                                    dsets[sets][el]['prod_label'] 
                                                                   ) 
                                                )
                    dsets[sets][el]['status'] = self.timestamp( environ['USER'][:-1] ) 
                    with open(self.datasets_path ,'wb') as FSO:
                        dump(dsets, FSO,indent=4)
                    return

        raise Warning('No more jobs')

#################################################################################

#job = DatasetChooser('../steerUtils/datasets.json')
#job.GetOpenJob()

#tag = job.strTag
#dataset = job.strDatacard

tag = "SUSYGluGluToHToTauTau_MCSpring16_pythia8_160621"
dataset = '/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM'
config = Configuration()
config.section_("General")
config.General.requestName = tag

config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'runMVAMET.py'
config.JobType.inputFiles = ['Spring16_25nsV3_MC.db']

config.section_("Data")
config.Data.inputDataset = dataset
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
#config.Data.publication = False
# This string is used to construct the output dataset name
config.Data.outputDatasetTag = tag
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
#config.Site.whitelist = ["T2_AT_Vienna"]
#config.Site.blacklist = ['T2_US_Purdue', 'T2_BE_IIHE', 'T2_US_Wisconsin', 'T2_UK_SGrid_Bristol', 'T2_US_Nebraska']
