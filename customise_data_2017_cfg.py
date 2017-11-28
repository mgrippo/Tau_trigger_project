import FWCore.ParameterSet.Config as cms

#from hlt_double_tau_asym_data_cfg import process # adapt to your case
from hlt92X_ZeroBias_my import process

process.source.fileNames          = cms.untracked.vstring([
    # put here your MINIAOD files
    '/store/data/Run2017F/ZeroBias/MINIAOD/06Nov2017-v1/150000/020A8867-F3C2-E711-876C-4C79BA1809AF.root',
])

process.source.secondaryFileNames = cms.untracked.vstring([
    # put here your RAW parent files
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/0237BBF2-B7BD-E711-925C-02163E013921.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/0AE36582-C4BD-E711-8E41-02163E019D19.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/1A683104-BABD-E711-B275-02163E011C2A.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/206B1EEB-B9BD-E711-88F2-02163E011BD0.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/227D12E5-BCBD-E711-B264-02163E01A283.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/382181EE-B7BD-E711-870F-02163E01A428.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/3A3F3E32-B5BD-E711-9B64-02163E01A25A.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/3C42F99E-CEBD-E711-AFFE-02163E01A413.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/4CD809E4-B9BD-E711-BAAC-02163E01469E.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/4E7FFE77-C9BD-E711-B357-02163E01372D.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/507390BA-D6BD-E711-A2A7-02163E01462F.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/5631416E-D6BD-E711-8C90-02163E013841.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/5CD26463-CBBD-E711-9147-02163E013807.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/70556064-CEBD-E711-8381-02163E01410E.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/86F7638A-C4BD-E711-8A0D-02163E0144E9.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/92A2FA67-CBBD-E711-8552-02163E019DAA.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/92C2084B-D8BD-E711-B92B-02163E019DAA.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/A2922ED5-CFBD-E711-A99B-02163E011F8E.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/A6D2A8A7-C6BD-E711-82FF-02163E0140FA.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/C8F5DF8F-CBBD-E711-A796-02163E01360C.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/CA8DF28A-C9BD-E711-B6A4-02163E011E3E.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/CAB4A0FE-B7BD-E711-A3EE-02163E014188.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/D6D41991-C6BD-E711-9CF8-02163E011A45.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/DE08051E-B3BD-E711-BE10-02163E019B53.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/E69C495C-D0BD-E711-8FE3-02163E0144D3.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/E84561C7-BBBD-E711-9BA6-02163E01A302.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/F00EF528-CDBD-E711-ABC7-02163E019D55.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/F0609541-D6BD-E711-9802-02163E01410E.root',
   '/store/data/Run2017F/ZeroBias/RAW/v1/000/305/898/00000/F8C1E661-C9BD-E711-B4A3-02163E01A340.root',
])

process.maxEvents.input = cms.untracked.int32(100)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# use offline beamspot
process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotProducer")

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

process.patTriggerUnpacker = cms.EDProducer("PATTriggerObjectStandAloneUnpacker",
                                            patTriggerObjectsStandAlone = cms.InputTag("patTriggerCustom"),
                                            triggerResults = cms.InputTag('TriggerResults'      , '', process_name),
                                            unpackFilterLabels = cms.bool(True)
                                            )
process.selectedPatTriggerCustom = cms.EDFilter(
                                                'PATTriggerObjectStandAloneSelector',
                                                cut = cms.string('!filterLabels.empty()'),
                                                src = cms.InputTag('patTriggerUnpacker')
                                                )

if not hasattr(process, 'HLTAnalyzerEndpath'):
    print 'added needed endpath'
    process.HLTAnalyzerEndpath = cms.EndPath(process.patTriggerCustom *process.patTriggerUnpacker* process.selectedPatTriggerCustom)
    process.HLTSchedule.append(process.HLTAnalyzerEndpath)
else:
    process.HLTAnalyzerEndpath += process.patTriggerCustom
    process.HLTAnalyzerEndpath += process.patTriggerUnpacker
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

# kill DQM
try:
    del process.dqmOutput
    del process.DQMOutput
except:
    print 'no DQM to kill'

# keep all the MINIAOD content, and the updated trigger collections
process.hltOutputFULL.outputCommands = cms.untracked.vstring(
     'drop *',
     ### MINIAOD CONTENT
     'keep patPackedCandidates_packedPFCandidates__RECO',
     'keep patMuons_slimmedMuons__RECO',
     'keep patJets_slimmedJets__RECO',
     'keep recoVertexs_offlineSlimmedPrimaryVertices__RECO',
     'keep patTriggerObjectStandAlones_slimmedPatTrigger__RECO',
     'keep patElectrons_slimmedElectrons__RECO',
     'keep patPackedCandidates_lostTracks__RECO',
     'keep patJets_slimmedJetsPuppi__RECO',
     'keep l1tTauBXVector_caloStage2Digis_Tau_RECO',
     'keep patTaus_slimmedTaus__RECO',
     'keep patPhotons_slimmedPhotons__RECO',
     'keep patCompositeCandidates_oniaPhotonCandidates_conversions_RECO',
     'keep patMETs_slimmedMETs__RECO',
     'keep patMETs_slimmedMETsPuppi__RECO',
     'keep patMETs_slimmedMETsNoHF__RECO',
     'keep l1tEtSumBXVector_caloStage2Digis_EtSum_RECO',
     'keep patTaus_slimmedTausBoosted__RECO',
     'keep l1tJetBXVector_caloStage2Digis_Jet_RECO',
     'keep l1tEGammaBXVector_caloStage2Digis_EGamma_RECO',
     'keep GlobalAlgBlkBXVector_gtStage2Digis__RECO',
     'keep HcalNoiseSummary_hcalnoise__RECO',
     'keep patJets_slimmedJetsAK8__RECO',
     'keep recoSuperClusters_reducedEgamma_reducedSuperClusters_RECO',
     'keep patJets_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_RECO',
     'keep recoCaloClusters_reducedEgamma_reducedEBEEClusters_RECO',
     'keep recoConversions_reducedEgamma_reducedConversions_RECO',
     'keep EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_RECO',
     'keep recoVertexCompositePtrCandidates_slimmedKshortVertices__RECO',
     'keep floatedmValueMap_offlineSlimmedPrimaryVertices__RECO',
     'keep l1tMuonBXVector_gmtStage2Digis_Muon_RECO',
     'keep patIsolatedTracks_isolatedTracks__RECO',
     'keep recoCaloClusters_reducedEgamma_reducedESClusters_RECO',
     'keep LumiScalerss_scalersRawToDigi__RECO',
     'keep recoVertexCompositePtrCandidates_slimmedSecondaryVertices__RECO',
     'keep EcalRecHitsSorted_reducedEgamma_reducedEERecHits_RECO',
     'keep patPackedCandidates_lostTracks_eleTracks_RECO',
     'keep EcalRecHitsSorted_reducedEgamma_reducedESRecHits_RECO',
     'keep recoConversions_reducedEgamma_reducedSingleLegConversions_RECO',
     'keep recoVertexCompositePtrCandidates_slimmedLambdaVertices__RECO',
     'keep l1extraL1EtMissParticles_l1extraParticles_MET_RECO',
     'keep l1extraL1EtMissParticles_l1extraParticles_MHT_RECO',
     'keep recoCSCHaloData_CSCHaloData__RECO',
     'keep recoGsfElectronCores_reducedEgamma_reducedGedGsfElectronCores_RECO',
     'keep recoBeamHaloSummary_BeamHaloSummary__RECO',
     'keep recoPhotonCores_reducedEgamma_reducedGedPhotonCores_RECO',
     'keep edmTriggerResults_TriggerResults__HLT',
     'keep l1extraL1MuonParticles_l1extraParticles__RECO',
     'keep GlobalExtBlkBXVector_gtStage2Digis__RECO',
     'keep recoBeamSpot_offlineBeamSpot__RECO',
     'keep l1extraL1EmParticles_l1extraParticles_NonIsolated_RECO',
     'keep l1extraL1JetParticles_l1extraParticles_Forward_RECO',
     'keep l1extraL1JetParticles_l1extraParticles_Central_RECO',
     'keep l1extraL1EmParticles_l1extraParticles_Isolated_RECO',
     'keep l1extraL1JetParticles_l1extraParticles_IsoTau_RECO',
     'keep l1extraL1JetParticles_l1extraParticles_Tau_RECO',
     'keep double_fixedGridRhoFastjetCentralNeutral__RECO',
     'keep double_fixedGridRhoFastjetAllCalo__RECO',
     'keep double_fixedGridRhoFastjetCentralCalo__RECO',
     'keep double_fixedGridRhoFastjetAll__RECO',
     'keep double_fixedGridRhoFastjetCentral__RECO',
     'keep l1extraL1HFRingss_l1extraParticles__RECO',
     'keep patPackedTriggerPrescales_patTrigger__RECO',
     'keep edmTriggerResults_TriggerResults__RECO',
     'keep patPackedTriggerPrescales_patTrigger_l1max_RECO',
     'keep patPackedTriggerPrescales_patTrigger_l1min_RECO',
     'keep double_fixedGridRhoFastjetCentralChargedPileUp__RECO',
     'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer__RECO',
     'keep double_fixedGridRhoAll__RECO',
     'keep L1GlobalTriggerReadoutRecord_gtDigis__RECO',
     'keep Strings_slimmedPatTrigger_filterLabels_RECO',
     'keep uint_bunchSpacingProducer__RECO',
     
     #### EXTRAS
     'keep *_TriggerResults_*_*'                                                       ,
     'keep *_addPileupInfo_*_*'                                                        ,
     'keep GenEventInfoProduct_generator__SIM'                                         ,
     'keep *TriggerObjectStandAlone_*_*_*'                                             ,
     'keep *_*atTrigger*_*_*'                                                          ,
     'keep *_hltTriggerSummaryAOD_*_*'                                                 ,
     'keep *_*Stage2*_*_*'                                                             ,
     'keep *PFTauDiscriminator_*Open*_*_*'                                             ,
     'keep double_*ixedGridRho*_*_*'                                                   ,
     'keep HcalNoiseSummary_hcalnoise__RECO'                                           ,
     'keep *BeamSpot_offlineBeamSpot__RECO'                                            ,
     'keep *_*limmed*__*'                                                              ,
     'keep *_lostTracks__*'                                                            ,
     'keep *_packedPFCandidates__*'                                                    ,
     'keep *_packedGenParticles__*'                                                    ,
     'keep *_prunedGenParticles__*'                                                    ,
     'keep unsignedint_bunchSpacingProducer__*'                                        ,
     'keep *_reducedEgamma_reducedGedGsfElectronCores_*'                               ,
     'keep *_reducedEgamma_reducedSuperClusters_*'                                     ,
     #     'keep *_hltPFTaus*_*_%s' %process_name                                            ,
     #     'keep *_hltPFTauCharged3HitsPtSum*_*_%s' %process_name                            ,
     #     'keep *_hltPFTauCharged5HitsPtSum*_*_%s' %process_name                            ,
     #     'keep *_hltPFTauCharged8HitsPtSum*_*_%s' %process_name                            ,
     #     'keep *_hltPFTauNeutralPtSum*_*_%s' %process_name                                 ,
     'keep *_hltPFTauPhotonPtOutsideSignalCone*_*_%s' %process_name                    ,
     'keep *_hltL2TauPixelIsoTagProducer_*_%s' %process_name                           ,
     'keep *_hltL2TauJetsIso_*_%s' %process_name                                       ,
     'keep *_hltL2TauIsoFilter_*_%s' %process_name                                     ,
     #     'keep *_hltL2TauOpenIsoFilter_*_%s' %process_name                                 ,
     #     'keep *_hltL2TausForPixelIsolation_*_%s' %process_name                            ,
     #     'keep *_hltPFTau20TrackPt1Reg_*_%s' %process_name                                 ,
     #     'keep *_hltPFTau20Track_*_%s' %process_name                                       ,
     #     'keep *_hltParticleFlow*_*_%s' %process_name                                      ,
     #     'keep LHEEventProduct_externalLHEProducer__LHE'                                   ,
     #     'keep *_hltL1JetsHLTDoublePFTauTrackPt0OpenIsolationMatchReg_*_%s' %process_name  ,
     #     'keep *_hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationMatchReg_*_%s' %process_name,
     #     'keep *_hltPFTausSansRefReg_*_%s' %process_name                                   ,
     #     'keep *_hltSelectedPFTausTrackPt0OpenIsolationReg_*_%s' %process_name             ,
     #     'keep *_hltSelectedPFTausTrackPt0Reg_*_%s' %process_name                          ,
     #     'keep *_hltSelectedPFTausTrackPt1MediumIsolationReg_*_%s' %process_name           ,
     #     'keep *_hltSelectedPFTausTrackPt1Reg_*_%s' %process_name                          ,
     #     'keep *_hltPFTauPUcorrDBeta0p2Cone0p8Reg_*_%s' %process_name                      ,
     #     'keep *_hltPFTauPUcorrRhoCone0p5Reg_*_%s' %process_name                           ,
     
     #     'keep *'                                                                          ,
)

process.hltOutputFULL.fileName = cms.untracked.string(
                                                      'outputFULL_data.root'
                                                      )

process.FULLOutput = cms.EndPath( process.hltOutputFULL )
