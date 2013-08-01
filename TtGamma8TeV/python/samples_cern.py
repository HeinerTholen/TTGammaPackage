"""
This file contains the samples located on pcac3b04 and cern afs.
Cross sections in picobarns.
Luminosity in inverse picobarns.
"""

import cmstoolsac3b.sample as smp

# this is already set as default in the cmssw configs.
import cmstoolsac3b.settings as settings
settings.cfg_common_builtins.update({
     "puWeight"     : "PUWeightTrue",
     "skipChecks"   : True
})

#path_pc = "file:/user/tholen/eventFiles/fromGrid20130502/"
path_pc = "file:/disk1/tholen/eventFiles/fromGrid20130618/"

ttbar_xsec = settings.ttbar_xsec
ttbar_xsec_err = settings.ttbar_xsec_err

class whiz2to5(smp.Sample):
    legend      = "t#bar{t}#gamma (Signal)"
    x_sec       = .9081 * 2.0
    n_events    = 1074860  
    input_files = path_pc + "whiz_*.root" # n_events!!!
    cfg_builtin = {"preSelOpt": "go4Whiz"}

class T_t(smp.Sample):
    legend      = "Single Top"
    x_sec       = 56.4
    n_events    = 99876
    input_files = path_pc + 'T_t_*.root'

class Tbar_t(smp.Sample):
    legend      = "Single Top"
    x_sec       = 30.7
    n_events    = 1935072
    input_files = path_pc + 'Tbar_t_*.root'

class T_tW(smp.Sample):
    legend      = "Single Top"
    x_sec       = 11.1
    n_events    = 497658
    input_files = path_pc + 'T_tW_*.root'
    cfg_add_lines = ['process.source.eventsToSkip = cms.untracked.VEventRange("1:1085:325342-1:1085:325342")']

class Tbar_tW(smp.Sample):
    legend      = "Single Top"
    x_sec       = 11.1
    n_events    = 493460
    input_files = path_pc + 'Tbar_tW_*.root'

# Kindonakis https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat8TeV
class TTJetsSignal(smp.Sample):
    enable      = False
    legend      = "t#bar{t}#gamma (Signal)"
    x_sec       = ttbar_xsec
    n_events    = 6854514 
    input_files = path_pc + 'TTJets_*.root'
    cfg_builtin = {"preSelOpt": "doOverlapRemoval"}

class TTJets(smp.Sample):
    legend      = "t#bar{t} inclusive"
    x_sec       = ttbar_xsec
    n_events    = 6854514
    input_files = path_pc + 'TTJets_*.root'
    cfg_builtin = {"preSelOpt": "doOverlapRemoval"}
#    cfg_add_lines = ['process.source.eventsToSkip = cms.untracked.VEventRange("1:58828:17644617-1:58828:17644617")']

class TTNLO(smp.Sample):
    legend      = "t#bar{t} inclusive"
    x_sec       = ttbar_xsec
    n_events    = 4900000
    input_files = path_pc + 'TTNLO_*.root'
    cfg_builtin = {"preSelOpt": "doOverlapRemoval"}
    cfg_add_lines = ["process.puWeight.isMCatNLO=cms.untracked.bool(True)"]

class TTNLOSignal(smp.Sample):
    enable      = False
    legend      = "t#bar{t}#gamma (Signal)"
    x_sec       = ttbar_xsec
    n_events    = 4900000
    input_files = path_pc + 'TTNLO_*.root'
    cfg_builtin = {"preSelOpt": "doOverlapRemoval"}
    cfg_add_lines = ["process.puWeight.isMCatNLO=cms.untracked.bool(True)"]

class WJets(smp.Sample):
    legend      = "W + Jets"
    x_sec       = 37509.
    n_events    = 57709905
    input_files = path_pc + 'WJets_*.root'

class DYJets(smp.Sample):
    legend      = "DY + Jets"
    x_sec       = 3503.71
    n_events    = 30307207 
    input_files = path_pc + 'DYJets_*.root'

class RunA(smp.Sample):
    is_data     = True
    legend      = "Data"
    lumi        = 889.301 #lumiCalc2
    input_files = path_pc + 'RunA_*.root'
    cfg_builtin = {}

class RunB(smp.Sample):
    is_data     = True
    legend      = "Data"
    lumi        = 4425.7 #558.738 + 3867. #lumiCalc2 
    input_files = path_pc + 'RunB_*.root'
    cfg_builtin = {}

class RunC(smp.Sample):
    is_data     = True
    legend      = "Data"
    lumi        = 7147.7 #lumiCalc2
    input_files = path_pc + 'RunC_*.root'
    cfg_builtin = {}

class RunD(smp.Sample):
    is_data     = True
    legend      = "Data"
    #lumi        = #pixelLumi
    lumi        = 7318. #lumiCalc2
    input_files = path_pc + 'RunD_*.root'
    cfg_builtin = {}


