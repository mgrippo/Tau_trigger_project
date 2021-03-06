import FWCore.ParameterSet.Config as cms

#from hlt_double_tau_asym_mc_cfg import process # adapt to your case
from hlt92X_VBF_my import process


process.source.fileNames          = cms.untracked.vstring([
    # put here your MINIAOD files
	'/store/mc/RunIISummer17MiniAOD/VBFHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/NZSFlatPU28to62_HIG07_92X_upgrade2017_realistic_v10-v1/70000/0080A67C-FBA4-E711-A8FE-00259029E84C.root',
])

process.source.secondaryFileNames = cms.untracked.vstring([
    # put here your RAW parent files
	'/store/mc/RunIISummer17DRStdmix/VBFHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/NZSFlatPU28to62_HIG07_92X_upgrade2017_realistic_v10-v1/710000/EC692FE1-DFA2-E711-8393-0025902BD8CE.root',
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
                                                      'outputFULL.root'
                                                      )

process.FULLOutput = cms.EndPath( process.hltOutputFULL )
