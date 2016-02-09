from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'heppy_crab_fake_pset.py'
config.JobType.scriptExe = 'heppy_crab_script.sh'
# config.JobType.sendPythonFolder = True  #doesn't work, not supported yet? do it by hand
import os
os.system("tar czf python.tar.gz --dereference --directory $CMSSW_BASE python")
os.system("tar czf cmgdataset.tar.gz --directory $HOME .cmgdataset")
os.system("tar czf cafpython.tar.gz --directory /afs/cern.ch/cms/caf/ python")
config.JobType.inputFiles = ['FrameworkJobReport.xml','heppy_crab_script.py','cmgdataset.tar.gz', 'python.tar.gz', 'cafpython.tar.gz', 'test.txt']
#config.JobType.outputFiles = ['output.log.tgz','test.txt'] # mt2.root is automatically send because of the pset file

config.section_("Data")
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
#config.Data.outLFNDirBase = '/store/user/jbrandst' 
config.Data.outputDatasetTag = ''
config.Data.publication = False

config.section_("Site")
#config.Site.whitelist = ["T2_CH_CSCS"]
config.Site.whitelist = ["T2_AT_Vienna"] #, "T2_FR_IPHC", "T2_BE_IIHE", "T2_IT_Pisa", "T2_ES_IFCA", "T2_UK_London_Brunel"] , "T2_PK_NCP", "T2_US_Purdue", "T2_UA_KIPT", "T2_KR_KNU", "T2_RU_IHEP", "T2_RU_INR", "T2_RU_JINR", "T2_US_MIT", "T2_US_Wisconsin", "T2_US_UCSD", "T2_US_Vanderbilt", "T2_US_Caltech"]
config.Site.storageSite = "T2_AT_Vienna"
#config.Data.ignoreLocality = True
