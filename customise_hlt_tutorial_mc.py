from hlt_tutorial_mc import *

# MINIAOD Z' to tau tau files (optional)
miniaod_zptt_relval = [
    '/store/relval/CMSSW_8_0_3/RelValZpTT_1500_13/MINIAODSIM/80X_mcRun2_asymptotic_2016_v3_gs7120p2NewGTv3-v1/00000/56A8CE64-CEEF-E511-AE04-0025905A60F8.root',
    '/store/relval/CMSSW_8_0_3/RelValZpTT_1500_13/MINIAODSIM/80X_mcRun2_asymptotic_2016_v3_gs7120p2NewGTv3-v1/00000/D042E561-CEEF-E511-BED8-0025905B8566.root',
]

# parent RAW Z' to tau tau files, necessary to rerun L1 emulation and HLT
raw_zptt_relval     = [
    '/store/relval/CMSSW_8_0_3/RelValZpTT_1500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_v3_gs7120p2NewGTv3-v1/00000/06A84CF7-C7EF-E511-9789-0025905B85DE.root',
    '/store/relval/CMSSW_8_0_3/RelValZpTT_1500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_v3_gs7120p2NewGTv3-v1/00000/0CE31440-C6EF-E511-A0DF-0025905B8600.root',
    '/store/relval/CMSSW_8_0_3/RelValZpTT_1500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_v3_gs7120p2NewGTv3-v1/00000/16735EFB-C7EF-E511-A671-0025905B85DC.root',
    '/store/relval/CMSSW_8_0_3/RelValZpTT_1500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_v3_gs7120p2NewGTv3-v1/00000/580757EC-C6EF-E511-A967-003048FF9ABC.root',
    '/store/relval/CMSSW_8_0_3/RelValZpTT_1500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_v3_gs7120p2NewGTv3-v1/00000/64890682-C6EF-E511-B93A-0CC47A4C8EC6.root',
    '/store/relval/CMSSW_8_0_3/RelValZpTT_1500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_2016_v3_gs7120p2NewGTv3-v1/00000/74B6A451-C6EF-E511-A333-0025905B8606.root',
]

process.source.fileNames          = cms.untracked.vstring(miniaod_zptt_relval)
process.source.secondaryFileNames = cms.untracked.vstring(raw_zptt_relval    )

process.maxEvents.input = cms.untracked.int32(100)

# keep all the MINIAOD content, and the updated trigger collections
process.hltOutputFULL.outputCommands = cms.untracked.vstring(
    'drop *'                                       ,
    'keep *_*_*_RECO'                              ,
    'keep *_*_*_PAT'                               ,
    'keep *_l1extraParticles_*_*'                  ,
    'keep *_TriggerResults_*_*'                    ,
    'keep *_addPileupInfo_*_*'                     ,
    'keep LHEEventProduct_externalLHEProducer__LHE',
    'keep GenEventInfoProduct_generator__SIM'      ,
    'keep *TriggerObjectStandAlone_*_*_*'          ,
    'keep *_hltL1extraParticles_*_*'               ,
    'keep *_selectedPatTriggerCustom_*_*'          ,
    'keep *_hltTriggerSummaryAOD_*_*'              ,
    'keep *_*Stage2*_*_*'                          ,
#     'keep *'                                       ,
)

process.hltOutputFULL.fileName = cms.untracked.string(
    'outputFULL_ZprimeTT.root'
)

# create PAT trigger objects using the updated trigger collections
from PhysicsTools.PatAlgos.tools.trigTools import *

if not hasattr(process, 'HLTAnalyzerEndpath'):
    process.HLTAnalyzerEndpath = cms.Path()

switchOnTriggerStandAlone(
    process                               ,
    path            = 'HLTAnalyzerEndpath',
    triggerProducer = 'patTriggerCustom'  ,
    hltProcess      = 'TEST'              ,
    outputModule    = 'hltOutputFULL'
)

process.selectedPatTriggerCustom = cms.EDFilter(
    'PATTriggerObjectStandAloneSelector',
    cut = cms.string('!filterLabels.empty()'),
    src = cms.InputTag('patTriggerCustom')
)

process.HLTAnalyzerEndpath.insert(1, process.selectedPatTriggerCustom)
process.HLTSchedule.insert(-1, process.HLTAnalyzerEndpath)

#
reportInterval = 1
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = reportInterval
