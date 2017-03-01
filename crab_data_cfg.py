from collections import OrderedDict
from zero_bias_datasets import zero_bias_datasets
from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.psetName        = 'customise_cfg.py'
config.JobType.pluginName      = 'Analysis'
config.JobType.outputFiles     = ['outputFULL.root']
config.JobType.maxMemoryMB     = 4000
config.JobType.priority        = 99999

config.Data.unitsPerJob        = 40
config.Data.splitting          = 'LumiBased'

config.Data.publication        = True
config.Data.outputDatasetTag   = 'doubleTauTriggerOpenPt'

config.Site.storageSite        = 'T2_CH_CERN'
# config.Site.blacklist          = ['T1_US_FNAL']
# config.Site.whitelist          = ['T2_CH_CERN']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'doubleTauTrigger'
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    datasets = zero_bias_datasets

    jsons = OrderedDict()
    
    jsons['lumi_1p05e34'] = 'jsons/ntuple_1p05e34.json'
    jsons['lumi_1p15e34'] = 'jsons/ntuple_1p15e34.json'
    jsons['lumi_1p25e34'] = 'jsons/ntuple_1p25e34.json'
    jsons['lumi_1p35e34'] = 'jsons/ntuple_1p35e34.json'
    jsons['lumi_1p45e34'] = 'jsons/ntuple_1p45e34.json'
    jsons['lumi_8p5e33' ] = 'jsons/ntuple_8p5e33.json'

    for kj, vj in jsons.iteritems():
        for k, v in datasets.iteritems():
            # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
            # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
            config.General.workArea   = 'crab_mc_' + tag + '_' + kj
            config.Data.outLFNDirBase = '/store/group/phys_tau/' + tag + '/' + kj
            config.Data.lumiMask = kj
            config.General.requestName = k
            config.Data.inputDataset = v[0]
            config.Data.secondaryInputDataset = v[1]
            print 'submitting config:'
            print config
            #submit(config)
            #import pdb ; pdb.set_trace()

