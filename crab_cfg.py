from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.psetName        = 'customise_anti_ele.py'
config.JobType.pluginName      = 'Analysis'
config.JobType.outputFiles     = ['outputFULL_ztt.root']
config.JobType.maxMemoryMB     = 2500
config.JobType.priority        = 99999

config.Data.unitsPerJob        = 12000
config.Data.splitting          = 'EventAwareLumiBased'

# JSON files:
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/
config.Data.publication        = True
config.Data.outputDatasetTag   = 'antiEleRate'

config.Site.storageSite        = 'T2_CH_CERN'
# config.Site.blacklist          = ['T1_US_FNAL']
# config.Site.whitelist          = ['T2_CH_CERN']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'antiEleRateV2'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea   = 'crab_mc_' + tag
    config.Data.outLFNDirBase = '/store/group/phys_tau/HLT2016/' + tag 
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    datasets = {}

    # datasets['DYJetsToLL']= ('/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM','/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16DR80-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v1/RAWAODSIM')
    datasets['DYJetsToLL_TSG'] = ('/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM', '/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/RunIISpring16DR80-FlatPU8to37HcalNZSRAW_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/GEN-SIM-RAW')


#     datasets['DYJetsToLL_25ns_PUFlat10to50']= ('dummy','/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-25nsFlat10to50ZsecalNzshcalRaw_76X_mcRun2_asymptotic_2016EcalTune_30fb_v1-v1/GEN-SIM-RAW')
#     datasets['DYJetsToLL_25ns_PUFlat10to25']= ('/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-25nsFlat10to25TSG_HCALDebug_76X_mcRun2_asymptotic_v11-v1/MINIAODSIM','/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-25nsFlat10to25TSG_HCALDebug_76X_mcRun2_asymptotic_v11-v1/GEN-SIM-RAW')
#     datasets['HLTPhysics2_Run2016B']= ('dummy','/HLTPhysics2/Run2016B-v1/RAW')
#     datasets['HLTPhysics3_Run2016B']= ('dummy','/HLTPhysics3/Run2016B-v1/RAW')

    for k, v in datasets.iteritems():
        config.General.requestName = k
        config.Data.inputDataset          = v[0]
        config.Data.secondaryInputDataset = v[1]
        print 'submitting config:'
        print config
        submit(config)

