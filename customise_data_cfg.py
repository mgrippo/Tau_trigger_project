import FWCore.ParameterSet.Config as cms

from hlt_myPathModified_mc import process # adapt to your case


process.source.fileNames          = cms.untracked.vstring([
    # put here your MINIAOD files
])

process.source.secondaryFileNames = cms.untracked.vstring([
    # put here your RAW parent files
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

