
import cmstoolsac3b.settings as settings
import cmstoolsac3b.postprocessing as ppc
import cmstoolsac3b.postproctools as ppt
import cmstoolsac3b.rendering as rnd
import plots_commons as com
import re


def generate_data_mc_comp_tools():
    """
    Generates postproctools by subclassing from ptt.FSStackPlotter.
    Walks over all samples and specific analyzer tokens.
    """
    #run_labels = settings.data_samples().keys()
    #run_labels.append(None) # all runs
    run_labels = [""]
    analyzer_pats = [
        re.compile("CrtlPlotPre"),
        re.compile("CrtlPlotInter"),
        re.compile("CrtlPlotPost"),
        re.compile("Nm1Plot"),
        re.compile("Nm2Plot"),
        re.compile("JetAna"),
#        re.compile("DataMCCompPhotons"),
        re.compile("DataMCJetCheck"),
        re.compile("DataMCMuonCheck"),
        re.compile("BkgTmpltPlot"),
#        re.compile("DataMCPhotonCheck"),
#        re.compile("WeightsCheck"),
        ]
    list_of_tools = []
    for at in analyzer_pats:
        for rl in run_labels:
#            sample_list = _make_stack_sample_list(rl)

            ############################################# log scale
            tool = ppt.FSStackPlotter(
                "DataMC_" + at.pattern + "_logscale" + rl
            )
            tool.filter_dict = {
                "analyzer": at,
#                "sample": sample_list
            }
            tool.canvas_decorators.append(com.LumiTitleBox)
            tool.save_log_scale = True
            if "DataMC" in at.pattern:
                tool.hook_post_canvas_build = hook_DataMC_canv_post_log
            if "Nm1Plot" == at.pattern:
                tool.hook_post_canvas_build = hook_Nm1Plot_conv_post_log
            list_of_tools.append(tool)

            ############################################# lin scale
            tool = ppt.FSStackPlotter(
                "DataMC_" + at.pattern + "_linscale" + rl
            )
            tool.filter_dict = {
                "analyzer": at,
#                "sample": sample_list
            }
            tool.canvas_decorators.append(com.LumiTitleBox)
            if "DataMC" in at.pattern:
                tool.hook_post_canvas_build = hook_DataMC_canv_post_lin
            if "CrtlPlotPost" == at.pattern:
                tool.hook_post_canvas_build = hook_CrtlPlotPost_conv_post_lin
            if "Nm1Plot" == at.pattern:
                tool.hook_pre_canvas_build = hook_DataMC_canv_pre_lin
            list_of_tools.append(tool)
    chain = ppc.PostProcChainIndie("DataMcComp")
    chain.add_tools(list_of_tools)
    return chain


############################################################ customizations ###
def hook_DataMC_canv_pre_lin(bldrs):
    for b in bldrs:
        if b.name == "Nm1PlotpassEleVeto_histo":
            b.get_decorator(rnd.Legend).dec_par["x_pos"] = .3 # move legend
        yield b

def hook_DataMC_canv_post_lin(bldrs):
    for b in bldrs:
        ratio_range_07_13(b)
        jet_mult_hook(b)
        yield b

def hook_DataMC_canv_post_log(bldrs):
    for b in bldrs:
        b.first_drawn.SetMaximum(13 * b.first_drawn.GetMaximum()) # legend
        if b.name[-4:] == "_Eta":
            b.first_drawn.SetMaximum(7 * b.first_drawn.GetMaximum()) # legend
        ratio_range_07_13(b)
        jet_mult_hook(b)
        yield b

def jet_mult_hook(bldr):
    if bldr.name == "DataMCJetCheckTrue_Mult":
        bldr.first_drawn.GetXaxis().SetRangeUser(3, 13)
        bldr.bottom_hist.GetXaxis().SetRangeUser(3, 13)
        bldr.bottom_hist.SetMaximum(2.5)

def ratio_range_07_13(bldr):
    bldr.bottom_hist.SetMinimum(0.7)
    bldr.bottom_hist.SetMaximum(1.3)

def hook_Nm1Plot_conv_post_log(bldrs):
    for b in bldrs:
        if b.name == "Nm1Plotdrjet_histo":
            b.first_drawn.GetXaxis().SetRangeUser(0, 3.9)
            b.bottom_hist.GetXaxis().SetRangeUser(0, 3.9)
        yield b

def hook_CrtlPlotPost_conv_post_lin(bldrs):
    for b in bldrs:
        if b.name == "CrtlPlotPosteta_histo":
            b.first_drawn.SetMaximum(1.3 * b.first_drawn.GetMaximum()) # legend
        yield b