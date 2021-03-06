import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [

       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_202_1_R1Y.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_213_1_VgB.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_204_1_m3K.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_209_1_iT4.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_211_1_XUn.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_217_1_OAy.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_212_1_XAr.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_214_1_mTU.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_215_1_kFn.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_216_1_127.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_221_1_EwT.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_218_1_P4R.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_223_1_FWd.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_224_1_GCx.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_219_2_OC4.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_21_1_MSt.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_220_1_liP.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_222_1_Bq7.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_229_1_1y8.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_225_1_jSV.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_226_1_MTH.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_227_1_vpX.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_228_1_2sZ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_233_1_8cw.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_22_1_WFL.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_230_1_zkq.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_231_1_TVC.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_237_3_z7q.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_238_1_2Xc.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_232_2_VmG.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_234_1_mYF.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_235_1_cuS.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_241_1_6YD.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_242_1_PJ3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_236_1_FJP.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_239_1_25w.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_245_1_yMo.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_23_1_f9n.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_240_1_gaZ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_243_1_M5I.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_244_1_jpd.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_246_1_Ipu.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_247_1_aB4.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_248_1_Hsp.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_249_1_1uN.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_24_1_Xow.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_254_1_tNu.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_255_1_vao.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_250_1_zhs.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_251_1_bM8.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_258_1_Gkp.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_259_1_v4m.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_252_1_VNP.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_260_1_kSP.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_253_1_SVZ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_256_1_00F.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_263_1_BmG.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_257_1_QWU.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_265_1_B4t.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_266_1_gtJ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_267_1_RyP.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_268_1_qnx.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_269_1_R3U.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_25_1_jOj.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_270_1_lq9.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_261_1_w0S.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_262_1_t4Z.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_264_1_ngj.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_26_1_FZB.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_275_1_EYF.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_271_1_Sis.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_277_1_e1V.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_272_1_UIw.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_279_1_ujn.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_27_1_XC3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_280_1_7Q8.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_273_1_bga.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_282_1_mF8.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_283_1_BET.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_284_1_zt2.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_274_1_C5U.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_276_1_Gws.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_287_1_VQf.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_278_1_FHe.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_281_1_a8m.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_28_1_tZ3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_285_1_f47.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_286_1_Eem.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_292_1_zjS.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_288_1_lq4.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_294_1_iLO.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_289_1_O6v.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_290_2_c0M.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_291_1_3uF.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_298_1_PvB.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_293_1_GQz.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_295_1_xIS.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_296_1_Gfy.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_300_1_0AE.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_301_1_54V.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_297_1_KCP.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_303_1_iX3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_304_1_YUQ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_305_1_BVX.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_306_1_OKX.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_307_1_07p.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_308_1_qbk.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_309_1_4wT.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_299_1_moQ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_29_1_xPc.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_311_1_yFk.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_312_1_o7s.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_313_1_FUJ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_2_1_EP3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_315_1_oML.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_316_2_vpn.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_317_1_OGV.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_302_1_bpp.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_319_1_WVC.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_30_1_tZS.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_320_1_Xjl.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_310_1_DKK.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_322_1_QJR.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_314_1_Rnc.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_324_1_cKG.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_318_1_vOF.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_326_1_y8d.root' ] );

secFiles.extend( [
               ] )

