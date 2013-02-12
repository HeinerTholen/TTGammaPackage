import FWCore.ParameterSet.Config as cms

BTagRequirement = cms.EDFilter(
    "PATJetRefSelector",
    src = cms.InputTag("selectedPatJetsPF"),
    cut = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags") > 0.679'),
    filter = cms.bool(True)
)