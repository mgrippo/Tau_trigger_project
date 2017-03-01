from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.psetName        = 'customise_cfg.py'
config.JobType.pluginName      = 'Analysis'
config.JobType.outputFiles     = ['outputFULL_htt.root']
config.JobType.maxMemoryMB     = 2500
config.JobType.priority        = 99999

config.Data.unitsPerJob        = 12000
config.Data.splitting          = 'EventAwareLumiBased'

# JSON files:
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/
config.Data.publication        = True
config.Data.outputDatasetTag   = 'doubleTauTrigger'

config.Site.storageSite        = 'T2_CH_CERN'
# config.Site.blacklist          = ['T1_US_FNAL']
# config.Site.whitelist          = ['T2_CH_CERN']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'doubleTauTrigger'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea   = 'crab_mc_' + tag
    config.Data.outLFNDirBase = '/store/group/phys_tau/' + tag
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    datasets = {}

    datasets['VBFHToTauTau'] = ('/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-FlatPU28to62HcalNZSRAW_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', 
                                '/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16DR80-FlatPU28to62HcalNZSRAW_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/GEN-SIM-RAW')
   
    for k, v in datasets.iteritems():
        config.General.requestName = k
        config.Data.inputDataset          = v[0]
        config.Data.secondaryInputDataset = v[1]
        print 'submitting config:'
        print config
        submit(config)

