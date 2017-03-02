import FWCore.ParameterSet.Config as cms

from hlt_double_tau_open_pt_v7_data_cfg import process # adapt to your case


process.source.fileNames          = cms.untracked.vstring([
    # put here your MINIAOD files
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/MINIAOD/23Sep2016-v1/100000/020197DC-6987-E611-8BCB-008CFA197C38.root',
])

process.source.secondaryFileNames = cms.untracked.vstring([
    # put here your RAW parent files
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/278/875/00000/08984CA8-9763-E611-910E-FA163E28898E.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/278/875/00000/0E35D6E9-9C63-E611-9E9C-FA163E7FB4F5.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/278/975/00000/940D2C7C-EB64-E611-A090-02163E011B97.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/029/00000/3636DCF4-BF65-E611-AEBA-02163E014192.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/115/00000/2E36E6B2-2B67-E611-8F31-FA163EE43532.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/694/00000/7A125B12-746D-E611-8B5A-FA163E8CCDC0.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/694/00000/C66ACCAD-726D-E611-9487-FA163E1031EB.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/694/00002/BA4B4256-6B6D-E611-8CDC-02163E011EE8.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/716/00000/0CBEAE96-A46D-E611-9F7A-FA163E184B10.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/716/00000/6E982A07-A96D-E611-B028-02163E0135FB.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/716/00000/6ED0C7BA-A76D-E611-B5F6-02163E01420E.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/716/00000/C45E15B6-A76D-E611-8E32-02163E01394C.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/26462D94-7B6E-E611-A2F9-02163E014700.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/682ED06C-856E-E611-ADA4-02163E01360C.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/6CD22259-8F6E-E611-9F96-FA163EF437E8.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/6E266E1B-866E-E611-B536-02163E0118A9.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/7A23EDD8-8B6E-E611-803C-FA163E759B34.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/94693415-6C6E-E611-B712-02163E01468A.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/BAB3B7C1-806E-E611-A660-FA163EAAD2D1.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/D854BFB1-796E-E611-9EDC-02163E014623.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/D88B90D9-766E-E611-B116-02163E014157.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/766/00000/E235A881-806E-E611-9EE3-02163E011CBA.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/841/00000/40EF3FB5-0570-E611-9859-FA163E371E58.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/841/00000/5ABAE451-F86F-E611-80AD-02163E01295A.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/841/00000/62487351-0170-E611-8836-02163E0122C7.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/841/00000/9E663EF2-0370-E611-9154-FA163E4DB46A.root',
    'root://cms-xrd-global.cern.ch//store/data/Run2016G/JetHT/RAW/v1/000/279/841/00000/BC9FA6B8-0070-E611-987F-02163E014526.root',
])

process.maxEvents.input = cms.untracked.int32(-1)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# save only taus with some non too small pt
process.hltDoublePFTau35TrackPt1MediumCombinedIsolationDz02Reg.JetMinPt = cms.double( 20. )


# create new trigger objects from your trigger results
process_name = process.name_()
process.patTriggerCustom = cms.EDProducer(
    'PATTriggerProducer',
    TriggerResults              = cms.InputTag('TriggerResults'      , '', process_name),
    hltTriggerSummaryAOD        = cms.InputTag('hltTriggerSummaryAOD', '', process_name),
    l1tAlgBlkInputTag           = cms.InputTag('hltgtStage2Digis'    , '', process_name),
    l1tExtBlkInputTag           = cms.InputTag('hltgtStage2Digis'    , '', process_name),
    onlyStandAlone              = cms.bool(True),
    packTriggerPathNames        = cms.bool(True),
    processName                 = cms.string(process_name)
)

process.selectedPatTriggerCustom = cms.EDFilter(
    'PATTriggerObjectStandAloneSelector',
    cut = cms.string('!filterLabels.empty()'),
    src = cms.InputTag('patTriggerCustom')
)

if not hasattr(process, 'HLTAnalyzerEndpath'):
    print 'added needed endpath'
    process.HLTAnalyzerEndpath = cms.EndPath(process.patTriggerCustom * process.selectedPatTriggerCustom)
    process.HLTSchedule.append(process.HLTAnalyzerEndpath)
else:
    process.HLTAnalyzerEndpath += process.patTriggerCustom
    process.HLTAnalyzerEndpath += process.selectedPatTriggerCustom

reportInterval = 1
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = reportInterval


# adjust the ouput module
process.hltOutputFULL = cms.OutputModule( 'PoolOutputModule',
    fileName = cms.untracked.string( 'outputFULL.root' ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string( 'RECO' ),
        filterName = cms.untracked.string( '' )
    ),
    outputCommands = cms.untracked.vstring( 'keep *' ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('HLT_*',)
    )
)

# keep all the MINIAOD content, and the updated trigger collections
process.hltOutputFULL.outputCommands = cms.untracked.vstring(
    'drop *'                                                              ,
    'keep *_TriggerResults_*_*'                                           ,
    'keep *_addPileupInfo_*_*'                                            ,
    'keep LHEEventProduct_externalLHEProducer__LHE'                       ,
    'keep GenEventInfoProduct_generator__SIM'                             ,
    'keep *TriggerObjectStandAlone_*_*_*'                                 ,
    'keep *_*atTrigger*_*_*'                                              ,
    'keep *_hltTriggerSummaryAOD_*_*'                                     ,
    'keep *_*Stage2*_*_*'                                                 ,
    'keep *PFTauDiscriminator_*Open*_*_*'                                 ,
    'keep double_*ixedGridRho*_*_*'                                       ,
    'keep *_hltL1JetsHLTDoublePFTauTrackPt0OpenIsolationMatchReg_*_TEST'  ,
    'keep *_hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationMatchReg_*_TEST',
    'keep *_hltPFTausReg_*_TEST'                                          ,
    'keep *_hltPFTausSansRefReg_*_TEST'                                   ,
    'keep *_hltSelectedPFTausTrackPt0OpenIsolationReg_*_TEST'             ,
    'keep *_hltSelectedPFTausTrackPt0Reg_*_TEST'                          ,
    'keep *_hltSelectedPFTausTrackPt1MediumIsolationReg_*_TEST'           ,
    'keep *_hltSelectedPFTausTrackPt1Reg_*_TEST'                          ,
    'keep GenEventInfoProduct_generator__SIM'                             ,
    'keep HcalNoiseSummary_hcalnoise__RECO'                               ,
    'keep *BeamSpot_offlineBeamSpot__RECO'                                ,
    'keep *_*limmed*__*'                                                  ,
    'keep *_lostTracks__*'                                                ,
    'keep *_packedPFCandidates__*'                                        ,
    'keep *_packedGenParticles__*'                                        ,
    'keep *_prunedGenParticles__*'                                        ,
    'keep unsignedint_bunchSpacingProducer__*'                            ,
    'keep *_reducedEgamma_reducedGedGsfElectronCores_*'                   ,
    'keep *_reducedEgamma_reducedSuperClusters_*'                         ,

    'keep *_hltPFTauCharged3HitsPtSumReg_*_TEST'                          ,
    'keep *_hltPFTauCharged5HitsPtSumReg_*_TEST'                          ,
    'keep *_hltPFTauCharged8HitsPtSumReg_*_TEST'                          ,
    'keep *_hltPFTauNeutralPtSumReg_*_TEST'                               ,
    'keep *_hltPFTauPUcorrDBeta0p2Cone0p8Reg_*_TEST'                      ,
    'keep *_hltPFTauPUcorrRhoCone0p5Reg_*_TEST'                           ,
    'keep *_hltPFTauPhotonPtOutsideSignalConeReg_*_TEST'                  ,
    
    'keep *_hltParticleFlowReg_*_*'                                       ,
#     'keep *'                                       ,                   
)

process.hltOutputFULL.fileName = cms.untracked.string(
    'outputFULL.root'
)

process.FULLOutput = cms.EndPath( process.hltOutputFULL )

