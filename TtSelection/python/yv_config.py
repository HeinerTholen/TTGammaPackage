

import operator
from FWCore.ParameterSet import Config as cms

from MyPackage.TtSelection.yv_options import options
options = options()
options.isData = cms_var["is_data"]

process = cms.Process( 'PAT2' )
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.MessageLogger.categories+=(['EventInfo'])
#process.MessageLogger.categories+=(['MuonInfo'])
process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('EGamma.EGammaAnalysisTools.electronIdMVAProducer_cfi')
process.load('EGamma.EGammaAnalysisTools.electronIsolatorFromEffectiveArea_cfi')

# from Burt Betchart:
# https://twiki.cern.ch/twiki/bin/view/CMS/TwikiTopRefHermeticTopProjections
process.load('TopQuarkAnalysis.TopRefTuple.vertex_cff')
process.load('TopQuarkAnalysis.TopRefTuple.cleaning_cff')

process.source = cms.Source('PoolSource', fileNames = cms.untracked.vstring("") )
process.out = cms.OutputModule( "PoolOutputModule", 
    outputCommands = cms.untracked.vstring( 'keep *' ), 
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('patreco') ), 
    fileName=cms.untracked.string("SynchSelMuJets.root")
)
process.outskim = cms.OutputModule( "PoolOutputModule", 
    outputCommands = cms.untracked.vstring( 
        'drop *',
        'keep *_selectedPatJetsForAnalysis_*_*',
        'keep *_patPhotons_*_*', 'keep *_tightmuons_*_*',
        'keep *_addPileupInfo_*_*',
        'keep *_*OfflinePrimaryVertices*_*_*',
        'keep *_selectedPatElectronsTR_*_*',
        'keep *_patElectronsTR_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_offlineBeamSpot_*_*'
    ), 
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('patreco') ), 
    fileName=cms.untracked.string("/net/scratch_cms/institut_3b/kuessel/skimPU/"+cms_var["sample"]+"SynchSelMuJetsSkim.root")
)
process.add_( 
    cms.Service( "TFileService", 
        fileName = cms.string( options.output ), 
        closeFileFast = cms.untracked.bool(True) 
    ) 
)

from TopQuarkAnalysis.TopRefTuple.pf2pat import TopRefPF2PAT
topPF2PAT = TopRefPF2PAT(process,options) #configuration object for patPF2PATSequence

process.GlobalTag.globaltag = options.globalTag + '::All'
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool( not options.quiet ))
process.MessageLogger.cerr.FwkReport.reportEvery = 1000 if options.quiet else 10
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32( options.maxEvents ))
if not options.isData : process.eventCleaning.remove( process.scrapingFilter )
for item in ['mvaNonTrigV0'] : delattr( process, item )

process.patreco = cms.Path( reduce(operator.add, [getattr(process, item) for item in ['goodOfflinePrimaryVertices',
                                                                                      'eventCleaning',
                                                                                      'mvaTrigV0',
                                                                                      'patPF2PATSequence'+options.postfix]]))

process.load('TopQuarkAnalysis.TopRefTuple.lumi_cfi')
#from TopQuarkAnalysis.TopRefTuple.tuple import Tuple
#process.tuple = Tuple(process, options).path()

#begin yvi changes

#add volkers cuts
 
process.tightmuons=process.selectedPatMuonsTR.clone(cut = cms.string('isPFMuon && isGlobalMuon && pt > 26. && abs(eta) < 2.1 && globalTrack.normalizedChi2 < 10. && track.hitPattern.trackerLayersWithMeasurement > 5 && globalTrack.hitPattern.numberOfValidMuonHits > 0 && abs(dB) < 0.2 && innerTrack.hitPattern.numberOfValidPixelHits > 0 && numberOfMatchedStations > 1 && (chargedHadronIso + max(0.,neutralHadronIso+photonIso-0.5*puChargedHadronIso))/pt < 0.12'))


process.patreco +=process.tightmuons
process.TightMuon=cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(1),
    src = cms.InputTag("tightmuons"),
    minNumber = cms.uint32(1)
)
process.patreco +=process.TightMuon
process.MuonVeto = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(1),
    src = cms.InputTag("selectedPatMuonsTR"),
    minNumber = cms.uint32(1)
)
process.patreco += process.MuonVeto

#
#
#
process.ElectronVeto = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(0),
    src = cms.InputTag("selectedPatElectronsTR"),
    minNumber = cms.uint32(0)
)
process.patreco += process.ElectronVeto
process.selectedPatJetsForAnalysis55=process.selectedPatJetsForAnalysis.clone(src="selectedPatJetsForAnalysis", cut="pt>55")
process.patreco +=process.selectedPatJetsForAnalysis55
process.selectedPatJetsForAnalysis45=process.selectedPatJetsForAnalysis55.clone(cut="pt>45")
process.patreco +=process.selectedPatJetsForAnalysis45
process.selectedPatJetsForAnalysis35=process.selectedPatJetsForAnalysis55.clone(cut="pt>35")
process.patreco +=process.selectedPatJetsForAnalysis35
process.selectedPatJetsForAnalysis20=process.selectedPatJetsForAnalysis55.clone(cut="pt>20")
process.patreco +=process.selectedPatJetsForAnalysis20
process.selectedPatJetsForAnalysisBTag=process.selectedPatJetsForAnalysis55.clone(cut="pt>20 && bDiscriminator('combinedSecondaryVertexBJetTags') > 0.679")
process.patreco +=process.selectedPatJetsForAnalysisBTag
process.OneJet = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(10000),
    src = cms.InputTag("selectedPatJetsForAnalysis55"),
    minNumber = cms.uint32(1)
)
process.patreco += process.OneJet
process.TwoJet = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(10000),
    src = cms.InputTag("selectedPatJetsForAnalysis45"),
    minNumber = cms.uint32(2)
)
process.patreco += process.TwoJet
process.ThreeJet = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(10000),
    src = cms.InputTag("selectedPatJetsForAnalysis35"),
    minNumber = cms.uint32(3)
)
process.patreco += process.ThreeJet
process.FourJet = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(10000),
    src = cms.InputTag("selectedPatJetsForAnalysis20"),
    minNumber = cms.uint32(4)
)
process.patreco += process.FourJet
process.BTagJet = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(10000),
    src = cms.InputTag("selectedPatJetsForAnalysisBTag"),
    minNumber = cms.uint32(1)
)
#if options.skim:
process.patreco += process.BTagJet


if not options.isData:
    process.patreco.replace(process.pfAllPhotonsTR, process.pfAllPhotonsTR * process.photonMatch * process.patPhotons)
else:
    process.patPhotons.addGenMatch = False
    process.patreco.replace(process.pfAllPhotonsTR, process.pfAllPhotonsTR * process.patPhotons)

#some extra matching
process.photonMatchOthers = process.photonMatch.clone(
    mcPdgId     = cms.vint32(13, 21, 11, 1,2,3,4,5,6,
                            221,                        # eta 
                            211,                        # pion 
                             15,                        # tau       
                            311,                        # K 0
                            421,                        # D 0      
                            411,                        # D         
                            113,                        # rho 
                            223,                        # omega
                            333,                        # phi       
                            423,                        # D*(2007)  
                            111),                       # pion 0
    mcStatus    = cms.vint32(1),
    checkCharge = cms.bool(False),
    resolveAmbiguities = cms.bool(True), 
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = cms.double(0.2), 
    maxDPtRel = cms.double(1)
)


process.photonMatchAll = process.photonMatchOthers.clone(
    mcPdgId     = cms.vint32(22,
                            13, 21, 11, 1,2,3,4,5,6,
                            221,                        # eta 
                            211,                        # pion 
                             15,                        # tau       
                            311,                        # K 0
                            421,                        # D 0      
                            411,                        # D         
                            113,                        # rho 
                            223,                        # omega
                            333,                        # phi       
                            423,                        # D*(2007)  
                            111),                       # pion 0
)

process.patPhotonsOthersMatch = process.patPhotons.clone(
    genParticleMatch = cms.InputTag("photonMatchOthers")
)

process.patPhotonsAllMatch = process.patPhotons.clone(
    genParticleMatch = cms.InputTag("photonMatchAll")
)

if not options.isData:
    process.patreco.replace(
        process.patPhotons, 
        process.patPhotons 
        * process.photonMatchOthers 
        * process.photonMatchAll
        * process.patPhotonsOthersMatch
        * process.patPhotonsAllMatch
    )  
process.outPath=cms.Path()
#if options.outputModule:
#   if options.skim:
#       process.outPath=cms.EndPath(process.outskim)
#   else:
process.outPath = cms.EndPath(process.out)

#end yvi changes

process.schedule = cms.Schedule( process.patreco,
                                 #process.tuple,
                                 process.lumi,
                                 process.outPath
)

# dump config
process.prune()
delattr(process,'PF2PAT')
with open(options.output.replace('.root','_cfg.py'),'w') as cfg : print >>cfg, process.dumpPython()



# investigate events

#process.printEventInfoStep1=cms.EDAnalyzer("PrintEventInfo", srcMuons=cms.untracked.InputTag("tightmuons"))
#process.patreco.replace(process.TightMuon, process.TightMuon * process.printEventInfoStep1)

# jet smearing details
process.load("PhysicsTools.PatAlgos.patSequences_cff")
from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties
runMEtUncertainties(process)
process.smearedPatJets.src="patJetsTR"

process.connectedJets = cms.EDProducer("PATJetCleaner",
    src = cms.InputTag("smearedPatJets"), 
    preselection = process.selectedPatJetsForAnalysis20.cut,
    checkOverlaps = cms.PSet(
        unsmearedJets = cms.PSet(
           src       = cms.InputTag("patJetsTR"),
           algorithm = cms.string("byDeltaR"),
           preselection        = process.selectedPatJetsForAnalysis20.cut,  
           deltaR              = cms.double(0.5),
           checkRecoComponents = cms.bool(False), # don't check if they share some AOD object ref
           pairCut             = cms.string(""),
           requireNoOverlaps   = cms.bool(False), # overlaps don't cause the jet to be discared
        )
    ),
    finalCut = cms.string(''),
)
process.OverlapJets=process.selectedPatJetsForAnalysis.clone(src="connectedJets", cut="hasOverlaps('unsmearedJets') && overlaps('unsmearedJets')[0].pt >0")

process.ResFactorsJets= cms.EDAnalyzer( "CandViewHistoAnalyzer",
                                        src = cms.InputTag("OverlapJets"),                                        
                                        histograms = cms.VPSet(
    cms.PSet(min          = cms.untracked.double(       0.9),
             max          = cms.untracked.double(      1.1),
             nbins        = cms.untracked.int32 (       100),
             name         = cms.untracked.string('res-factors'),
             description  = cms.untracked.string('res;smear pt / unsmear pt;Number of jets'),
             lazyParsing  = cms.untracked.bool(True),
             plotquantity = cms.untracked.string(" pt / overlaps('unsmearedJets')[0].pt")
             )
    )
                                        )
process.NumOverlaps= cms.EDAnalyzer( "CandViewHistoAnalyzer",
                                        src = cms.InputTag("OverlapJets"),                                        
                                        histograms = cms.VPSet(
    cms.PSet(min          = cms.untracked.double(       -0.5),
             max          = cms.untracked.double(      4.5),
             nbins        = cms.untracked.int32 (       5),
             name         = cms.untracked.string('number of matched'),
             description  = cms.untracked.string('number of overlaps;number of overlaps;Number of jets'),
             lazyParsing  = cms.untracked.bool(True),
             plotquantity = cms.untracked.string(" overlaps('unsmearedJets').size")
             )
    )
                                        )
process.NumConnectedJets= cms.EDAnalyzer( "CandViewHistoAnalyzer",
                                        src = cms.InputTag("connectedJets"),                                        
                                        histograms = cms.VPSet(
    cms.PSet(min          = cms.untracked.double(       0.),
             max          = cms.untracked.double(      200.),
             nbins        = cms.untracked.int32 (       100),
             name         = cms.untracked.string('number of connectedJets'),
             description  = cms.untracked.string('number of connectedJets;pt;Number of jets'),
             lazyParsing  = cms.untracked.bool(True),
             plotquantity = cms.untracked.string(" pt")
             )
    )
                                        )
if not options.isData:
     print "Smear Jets."
     process.selectedPatJetsForAnalysis.src="smearedPatJets"
     process.patreco.replace(process.selectedPatJetsForAnalysis,process.smearedPatJets * process.selectedPatJetsForAnalysis)

#* process.connectedJets * process.OverlapJets * process.ResFactorsJets * process.NumOverlaps * process.NumConnectedJets)
