import FWCore.ParameterSet.Config as cms

from hlt_double_tau_asym_data_cfg import process # adapt to your case


process.source.fileNames          = cms.untracked.vstring([
    # put here your MINIAOD files
    'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/MINIAOD/06Nov2017-v1/150000/020A8867-F3C2-E711-876C-4C79BA1809AF.root',
])

process.source.secondaryFileNames = cms.untracked.vstring([
    # put here your RAW parent files
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/0237BBF2-B7BD-E711-925C-02163E013921.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/0AE36582-C4BD-E711-8E41-02163E019D19.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/1A683104-BABD-E711-B275-02163E011C2A.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/206B1EEB-B9BD-E711-88F2-02163E011BD0.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/227D12E5-BCBD-E711-B264-02163E01A283.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/382181EE-B7BD-E711-870F-02163E01A428.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/3A3F3E32-B5BD-E711-9B64-02163E01A25A.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/3C42F99E-CEBD-E711-AFFE-02163E01A413.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/4CD809E4-B9BD-E711-BAAC-02163E01469E.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/4E7FFE77-C9BD-E711-B357-02163E01372D.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/507390BA-D6BD-E711-A2A7-02163E01462F.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/5631416E-D6BD-E711-8C90-02163E013841.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/5CD26463-CBBD-E711-9147-02163E013807.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/70556064-CEBD-E711-8381-02163E01410E.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/86F7638A-C4BD-E711-8A0D-02163E0144E9.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/92A2FA67-CBBD-E711-8552-02163E019DAA.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/92C2084B-D8BD-E711-B92B-02163E019DAA.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/A2922ED5-CFBD-E711-A99B-02163E011F8E.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/A6D2A8A7-C6BD-E711-82FF-02163E0140FA.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/C8F5DF8F-CBBD-E711-A796-02163E01360C.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/CA8DF28A-C9BD-E711-B6A4-02163E011E3E.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/CAB4A0FE-B7BD-E711-A3EE-02163E014188.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/D6D41991-C6BD-E711-9CF8-02163E011A45.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/DE08051E-B3BD-E711-BE10-02163E019B53.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/E69C495C-D0BD-E711-8FE3-02163E0144D3.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/E84561C7-BBBD-E711-9BA6-02163E01A302.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/F00EF528-CDBD-E711-ABC7-02163E019D55.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/F0609541-D6BD-E711-9802-02163E01410E.root',
   'root://cms-xrd-global.cern.ch//store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/F8C1E661-C9BD-E711-B4A3-02163E01A340.root',
])

process.maxEvents.input = cms.untracked.int32(-1)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

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

