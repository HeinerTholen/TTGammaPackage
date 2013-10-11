// -*- C++ -*-
//
// Package:    BTagWeight
// Class:      BTagWeight
// 
/**\class BTagWeight BTagWeight.cc MyPackage/BTagWeight/src/BTagWeight.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Heiner Tholen,32 4-B20,+41227676487,
//         Created:  Sun Aug 18 18:01:25 CEST 2013
// $Id: BTagWeight.cc,v 1.3 2013/10/09 13:51:58 htholen Exp $
//
//



/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
// SFlight functions, see
// https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG
// and
// https://twiki.cern.ch/twiki/pub/CMS/BtagPOG/SFlightFuncs_EPS2013.C 
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////


#include "TF1.h"

//------------ Exemple of usage --------------
//
// In a root session:
// 	.L SFlightFuncs.C+g	//To load this program
// Then...
// To get a pointer to the SFlight function for CSV tagger Loose (L) in the eta range 0.0-0.5 for the data taking period A+B+C+D, use: 
//	TF1* SFlight = GetSFlmean("CSV","L",0.0, 0.5, "ABCD")
// To get a pointer to the SFlightmin function for CSV tagger Loose (L) in the eta range 0.0-0.5 for the data taking period A+B+C+D, use: 
//	TF1* SFlightmin = GetSFlmin("CSV","L",0.0, 0.5, "ABCD")
// To get a pointer to the SFlightmax function for CSV tagger Loose (L) in the eta range 0.0-0.5 for the data taking period A+B+C+D, use: 
//	TF1* SFlightmax = GetSFlmax("CSV","L",0.0, 0.5, "ABCD")
//
// Note:
// 1) SFlightmin and SFlightmax correspond to SFlight +- (stat+syst error).
// 2) If the specified combination of tagger/taggerstrength/etarange is not tabulated,
//    a NULL pointer is returned.
//
//-------------------------------------------
TF1* GetSFLight(TString meanminmax, TString tagger, TString TaggerStrength, Float_t Etamin, Float_t Etamax, TString DataPeriod);

TF1* GetSFlmean(TString tagger, TString TaggerStrength, float Etamin, float Etamax, TString DataPeriod)
{
  return GetSFLight("mean",tagger,TaggerStrength,Etamin,Etamax,DataPeriod);
}
TF1* GetSFlmin(TString tagger, TString TaggerStrength, float Etamin, float Etamax, TString DataPeriod)
{
  return GetSFLight("min",tagger,TaggerStrength,Etamin,Etamax,DataPeriod);
}
TF1* GetSFlmax(TString tagger, TString TaggerStrength, float Etamin, float Etamax, TString DataPeriod)
{
  return GetSFLight("max",tagger,TaggerStrength,Etamin,Etamax,DataPeriod);
}

// REMOVE FUNCTIONS FOR PLOTTING HERE 

TF1* GetSFLight(TString meanminmax, TString tagger, TString TaggerStrength, Float_t Etamin, Float_t Etamax, TString DataPeriod)
{
  TF1 *tmpSFl = NULL;

  TString Atagger = tagger+TaggerStrength;
  TString sEtamin = Form("%1.1f",Etamin);
  TString sEtamax = Form("%1.1f",Etamax);
  std::cout << sEtamin << std::endl;
  std::cout << sEtamax << std::endl;

  if( (TaggerStrength == "L" || TaggerStrength == "M") && sEtamin == "0.0" && sEtamax == "2.4" )
  {
    std::cout << "For L and M taggers, the function is not provided integrated over eta. Only eta subranges are provided " << std::endl;
    return tmpSFl;
  }

  Double_t ptmax;
  if( sEtamin == "1.5" || sEtamin == "1.6" ) ptmax = 850;
  else ptmax = 1000;

// Insert function def below here =====================================

if( Atagger == "CSVL" && sEtamin == "0.0" && sEtamax == "0.5")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.01177+(0.0023066*x))+(-4.56052e-06*(x*x)))+(2.57917e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.977761+(0.00170704*x))+(-3.2197e-06*(x*x)))+(1.78139e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.04582+(0.00290226*x))+(-5.89124e-06*(x*x)))+(3.37128e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVL" && sEtamin == "0.5" && sEtamax == "1.0")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.975966+(0.00196354*x))+(-3.83768e-06*(x*x)))+(2.17466e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.945135+(0.00146006*x))+(-2.70048e-06*(x*x)))+(1.4883e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.00683+(0.00246404*x))+(-4.96729e-06*(x*x)))+(2.85697e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVL" && sEtamin == "1.0" && sEtamax == "1.5")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.93821+(0.00180935*x))+(-3.86937e-06*(x*x)))+(2.43222e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.911657+(0.00142008*x))+(-2.87569e-06*(x*x)))+(1.76619e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((0.964787+(0.00219574*x))+(-4.85552e-06*(x*x)))+(3.09457e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVL" && sEtamin == "1.5" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.00022+(0.0010998*x))+(-3.10672e-06*(x*x)))+(2.35006e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.970045+(0.000862284*x))+(-2.31714e-06*(x*x)))+(1.68866e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.03039+(0.0013358*x))+(-3.89284e-06*(x*x)))+(3.01155e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVM" && sEtamin == "0.0" && sEtamax == "0.8")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.07541+(0.00231827*x))+(-4.74249e-06*(x*x)))+(2.70862e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.964527+(0.00149055*x))+(-2.78338e-06*(x*x)))+(1.51771e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.18638+(0.00314148*x))+(-6.68993e-06*(x*x)))+(3.89288e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVM" && sEtamin == "0.8" && sEtamax == "1.6")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.05613+(0.00114031*x))+(-2.56066e-06*(x*x)))+(1.67792e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.946051+(0.000759584*x))+(-1.52491e-06*(x*x)))+(9.65822e-10*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.16624+(0.00151884*x))+(-3.59041e-06*(x*x)))+(2.38681e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVM" && sEtamin == "1.6" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.05625+(0.000487231*x))+(-2.22792e-06*(x*x)))+(1.70262e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.956736+(0.000280197*x))+(-1.42739e-06*(x*x)))+(1.0085e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.15575+(0.000693344*x))+(-3.02661e-06*(x*x)))+(2.39752e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVT" && sEtamin == "0.0" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.00462+(0.00325971*x))+(-7.79184e-06*(x*x)))+(5.22506e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.845757+(0.00186422*x))+(-4.6133e-06*(x*x)))+(3.21723e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.16361+(0.00464695*x))+(-1.09467e-05*(x*x)))+(7.21896e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVV1L" && sEtamin == "0.0" && sEtamax == "0.5")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.03599+(0.00187708*x))+(-3.73001e-06*(x*x)))+(2.09649e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.995735+(0.00146811*x))+(-2.83906e-06*(x*x)))+(1.5717e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.0763+(0.00228243*x))+(-4.61169e-06*(x*x)))+(2.61601e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVV1L" && sEtamin == "0.5" && sEtamax == "1.0")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.987393+(0.00162718*x))+(-3.21869e-06*(x*x)))+(1.84615e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.947416+(0.00130297*x))+(-2.50427e-06*(x*x)))+(1.41682e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.02741+(0.00194855*x))+(-3.92587e-06*(x*x)))+(2.27149e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVV1L" && sEtamin == "1.0" && sEtamax == "1.5")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.950146+(0.00150932*x))+(-3.28136e-06*(x*x)))+(2.06196e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.91407+(0.00123525*x))+(-2.61966e-06*(x*x)))+(1.63016e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((0.986259+(0.00178067*x))+(-3.93596e-06*(x*x)))+(2.49014e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVV1L" && sEtamin == "1.5" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.01923+(0.000898874*x))+(-2.57986e-06*(x*x)))+(1.8149e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.979782+(0.000743807*x))+(-2.14927e-06*(x*x)))+(1.49486e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.05868+(0.00105264*x))+(-3.00767e-06*(x*x)))+(2.13498e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVV1M" && sEtamin == "0.0" && sEtamax == "0.8")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.06383+(0.00279657*x))+(-5.75405e-06*(x*x)))+(3.4302e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.971686+(0.00195242*x))+(-3.98756e-06*(x*x)))+(2.38991e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.15605+(0.00363538*x))+(-7.50634e-06*(x*x)))+(4.4624e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVV1M" && sEtamin == "0.8" && sEtamax == "1.6")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.03709+(0.00169762*x))+(-3.52511e-06*(x*x)))+(2.25975e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.947328+(0.00117422*x))+(-2.32363e-06*(x*x)))+(1.46136e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.12687+(0.00221834*x))+(-4.71949e-06*(x*x)))+(3.05456e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVV1M" && sEtamin == "1.6" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.01679+(0.00211998*x))+(-6.26097e-06*(x*x)))+(4.53843e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.922527+(0.00176245*x))+(-5.14169e-06*(x*x)))+(3.61532e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.11102+(0.00247531*x))+(-7.37745e-06*(x*x)))+(5.46589e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVV1T" && sEtamin == "0.0" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.15047+(0.00220948*x))+(-5.17912e-06*(x*x)))+(3.39216e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.936862+(0.00149618*x))+(-3.64924e-06*(x*x)))+(2.43883e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.36418+(0.00291794*x))+(-6.6956e-06*(x*x)))+(4.33793e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVSLV1L" && sEtamin == "0.0" && sEtamax == "0.5")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.06344+(0.0014539*x))+(-2.72328e-06*(x*x)))+(1.47643e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((1.01168+(0.000950951*x))+(-1.58947e-06*(x*x)))+(7.96543e-10*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.11523+(0.00195443*x))+(-3.85115e-06*(x*x)))+(2.15307e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVSLV1L" && sEtamin == "0.5" && sEtamax == "1.0")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.0123+(0.00151734*x))+(-2.99087e-06*(x*x)))+(1.73428e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.960377+(0.00109821*x))+(-2.01652e-06*(x*x)))+(1.13076e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.06426+(0.0019339*x))+(-3.95863e-06*(x*x)))+(2.3342e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVSLV1L" && sEtamin == "1.0" && sEtamax == "1.5")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.975277+(0.00146932*x))+(-3.17563e-06*(x*x)))+(2.03698e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.931687+(0.00110971*x))+(-2.29681e-06*(x*x)))+(1.45867e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.0189+(0.00182641*x))+(-4.04782e-06*(x*x)))+(2.61199e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVSLV1L" && sEtamin == "1.5" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.04201+(0.000827388*x))+(-2.31261e-06*(x*x)))+(1.62629e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.992838+(0.000660673*x))+(-1.84971e-06*(x*x)))+(1.2758e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.09118+(0.000992959*x))+(-2.77313e-06*(x*x)))+(1.9769e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVSLV1M" && sEtamin == "0.0" && sEtamax == "0.8")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.06212+(0.00223614*x))+(-4.25167e-06*(x*x)))+(2.42728e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.903956+(0.00121678*x))+(-2.04383e-06*(x*x)))+(1.10727e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.22035+(0.00325183*x))+(-6.45023e-06*(x*x)))+(3.74225e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVSLV1M" && sEtamin == "0.8" && sEtamax == "1.6")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.04547+(0.00216995*x))+(-4.579e-06*(x*x)))+(2.91791e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.900637+(0.00120088*x))+(-2.27069e-06*(x*x)))+(1.40609e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.19034+(0.00313562*x))+(-6.87854e-06*(x*x)))+(4.42546e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVSLV1M" && sEtamin == "1.6" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.991865+(0.00324957*x))+(-9.65897e-06*(x*x)))+(7.13694e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.868875+(0.00222761*x))+(-6.44897e-06*(x*x)))+(4.53261e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.11481+(0.00426745*x))+(-1.28612e-05*(x*x)))+(9.74425e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "CSVSLV1T" && sEtamin == "0.0" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.09494+(0.00193966*x))+(-4.35021e-06*(x*x)))+(2.8973e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.813331+(0.00139561*x))+(-3.15313e-06*(x*x)))+(2.12173e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.37663+(0.00247963*x))+(-5.53583e-06*(x*x)))+(3.66635e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "JPL" && sEtamin == "0.0" && sEtamax == "0.5")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.991991+(0.000898777*x))+(-1.88002e-06*(x*x)))+(1.11276e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.930838+(0.000687929*x))+(-1.36976e-06*(x*x)))+(7.94486e-10*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.05319+(0.00110776*x))+(-2.38542e-06*(x*x)))+(1.42826e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "JPL" && sEtamin == "0.5" && sEtamax == "1.0")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.96633+(0.000419215*x))+(-9.8654e-07*(x*x)))+(6.30396e-10*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.904781+(0.000324913*x))+(-7.2229e-07*(x*x)))+(4.52185e-10*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.0279+(0.00051255*x))+(-1.24815e-06*(x*x)))+(8.07098e-10*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "JPL" && sEtamin == "1.0" && sEtamax == "1.5")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.968008+(0.000482491*x))+(-1.2496e-06*(x*x)))+(9.02736e-10*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.914619+(0.000330357*x))+(-8.41216e-07*(x*x)))+(6.14504e-10*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.02142+(0.000633484*x))+(-1.6547e-06*(x*x)))+(1.18921e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "JPL" && sEtamin == "1.5" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.991448+(0.000765746*x))+(-2.26144e-06*(x*x)))+(1.65233e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.933947+(0.000668609*x))+(-1.94474e-06*(x*x)))+(1.39774e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.04894+(0.000861785*x))+(-2.57573e-06*(x*x)))+(1.90702e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "JPM" && sEtamin == "0.0" && sEtamax == "0.8")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.991457+(0.00130778*x))+(-2.98875e-06*(x*x)))+(1.81499e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.822012+(0.000908344*x))+(-1.89516e-06*(x*x)))+(1.1163e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.16098+(0.00170403*x))+(-4.07382e-06*(x*x)))+(2.50873e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "JPM" && sEtamin == "0.8" && sEtamax == "1.6")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.00576+(0.00121353*x))+(-3.20601e-06*(x*x)))+(2.15905e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.845597+(0.000734909*x))+(-1.76311e-06*(x*x)))+(1.16104e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.16598+(0.00168902*x))+(-4.64013e-06*(x*x)))+(3.15214e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "JPM" && sEtamin == "1.6" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.939038+(0.00226026*x))+(-7.38544e-06*(x*x)))+(5.77162e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.803867+(0.00165886*x))+(-5.19532e-06*(x*x)))+(3.88441e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.07417+(0.00285862*x))+(-9.56945e-06*(x*x)))+(7.66167e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "JPT" && sEtamin == "0.0" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((0.953235+(0.00206692*x))+(-5.21754e-06*(x*x)))+(3.44893e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.642947+(0.00180129*x))+(-4.16373e-06*(x*x)))+(2.68061e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.26372+(0.0023265*x))+(-6.2548e-06*(x*x)))+(4.20761e-09*(x*(x*x)))", 20.,ptmax);
}
if( Atagger == "TCHPT" && sEtamin == "0.0" && sEtamax == "2.4")
{
if( meanminmax == "mean" ) tmpSFl = new TF1("SFlight","((1.20175+(0.000858187*x))+(-1.98726e-06*(x*x)))+(1.31057e-09*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "min" ) tmpSFl = new TF1("SFlightMin","((0.968557+(0.000586877*x))+(-1.34624e-06*(x*x)))+(9.09724e-10*(x*(x*x)))", 20.,ptmax);
if( meanminmax == "max" ) tmpSFl = new TF1("SFlightMax","((1.43508+(0.00112666*x))+(-2.62078e-06*(x*x)))+(1.70697e-09*(x*(x*x)))", 20.,ptmax);
}

// Insert function def above here =====================================
  
  if( tmpSFl == NULL ) std::cout << "NULL pointer returned... Function seems not to exist" << std::endl;

  return tmpSFl;
}



/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
// CMSSW Producer starting from here
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////




















// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
//#include "DataFormats/Candidate/interface/Candidate.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"

//
// class declaration
//

class BTagWeight : public edm::EDProducer {
   public:
      explicit BTagWeight(const edm::ParameterSet&);
      ~BTagWeight();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      float scaleFactorB_CSVM(const float pt);
      float scaleFactorC_CSVM(const float pt);
      float scaleFactorB_CSVM_Err(const float pt);
      float scaleFactorUDSG_CSVM(const float pt, const float eta);
      float scaleFactor_CSVM(const pat::Jet& jet);

      float weightBin0(const std::vector<float> &btagSFs);
      float weightBin1(const std::vector<float> &btagSFs);
      float bTagWeight(const std::vector<float> &btagSFs);

      // ----------member data ---------------------------
      edm::InputTag src_;
      edm::InputTag weights_;
      bool emptyWeightInputTag_;
      int errorModeBC_;
      int errorModeUDSG_;
      bool twoBTagMode_;
      TH1D* partonFlavour_;
      TF1* SFlight08_;
      TF1* SFlight16_;
      TF1* SFlight24_;
      float ptmax_16_;
      float ptmax_24_;
      float sf_gt_ptmax_08_;
      float sf_gt_ptmax_16_;
      float sf_gt_ptmax_24_;
};

//
// constructors and destructor
//
BTagWeight::BTagWeight(const edm::ParameterSet& iConfig):
    src_(iConfig.getParameter<edm::InputTag>("src")),
    weights_(iConfig.getUntrackedParameter<edm::InputTag>("weights", edm::InputTag())),
    emptyWeightInputTag_(weights_.encode() == std::string("")),
    errorModeBC_(iConfig.getUntrackedParameter<int>("errorModeBC", 0)),
    errorModeUDSG_(iConfig.getUntrackedParameter<int>("errorModeUDSG", 0)),
    twoBTagMode_(iConfig.getUntrackedParameter<bool>("twoBTagMode", false))
{
    edm::Service<TFileService> fs;
    partonFlavour_ = fs->make<TH1D>("partonFlavour", ";partonFlavour;number of b-tagged jets", 45, -22.5, 22.5);
    ptmax_16_ = 1000.;
    ptmax_24_ = 850.;
    SFlight08_   = GetSFlmean("CSV","M",0.0, 0.8, "ABCD");
    SFlight16_   = GetSFlmean("CSV","M",0.8, 1.6, "ABCD");
    SFlight24_   = GetSFlmean("CSV","M",1.6, 2.4, "ABCD");
    sf_gt_ptmax_08_ = SFlight08_->Eval(ptmax_16_); 
    sf_gt_ptmax_16_ = SFlight16_->Eval(ptmax_16_);
    sf_gt_ptmax_24_ = SFlight24_->Eval(ptmax_24_);
    if (errorModeUDSG_ < 0) {
        SFlight08_   = GetSFlmin("CSV","M",0.0, 0.8, "ABCD"); 
        SFlight16_   = GetSFlmin("CSV","M",0.8, 1.6, "ABCD");
        SFlight24_   = GetSFlmin("CSV","M",1.6, 2.4, "ABCD");
        sf_gt_ptmax_08_ -= 2*(sf_gt_ptmax_08_ - SFlight08_->Eval(ptmax_16_)); 
        sf_gt_ptmax_16_ -= 2*(sf_gt_ptmax_16_ - SFlight16_->Eval(ptmax_16_));
        sf_gt_ptmax_24_ -= 2*(sf_gt_ptmax_24_ - SFlight24_->Eval(ptmax_24_));
    } else if (errorModeUDSG_ > 0) {
        SFlight08_   = GetSFlmax("CSV","M",0.0, 0.8, "ABCD");
        SFlight16_   = GetSFlmax("CSV","M",0.8, 1.6, "ABCD");
        SFlight24_   = GetSFlmax("CSV","M",1.6, 2.4, "ABCD");
        sf_gt_ptmax_08_ += 2*(SFlight08_->Eval(ptmax_16_) - sf_gt_ptmax_08_); 
        sf_gt_ptmax_16_ += 2*(SFlight16_->Eval(ptmax_16_) - sf_gt_ptmax_16_);
        sf_gt_ptmax_24_ += 2*(SFlight24_->Eval(ptmax_24_) - sf_gt_ptmax_24_);
    }
    produces<double>();
}


BTagWeight::~BTagWeight()
{
}

//
// member functions
//
float BTagWeight::scaleFactorB_CSVM(const float pt)
{
    return (
        0.939158+(0.000158694*pt))+(-2.53962e-07*(pt*pt)
    ) + (
        errorModeBC_ * scaleFactorB_CSVM_Err(pt)
    );
}


float BTagWeight::scaleFactorC_CSVM(const float pt)
{
    return (
        0.939158+(0.000158694*pt))+(-2.53962e-07*(pt*pt)
    ) + (
        errorModeBC_ * 2 * scaleFactorB_CSVM_Err(pt)
    );
}


float BTagWeight::scaleFactorB_CSVM_Err(const float pt)
{
    static const float ptmax[] = {
        30.,
        40.,
        50.,
        60.,
        70.,
        80.,
        100.,
        120.,
        160.,
        210.,
        260.,
        320.,
        400.,
        500.,
        600.,
        800.,
        9999999.
    };
    static const float SFb_error[] = {
        0.0415694,
        0.023429,
        0.0261074,
        0.0239251,
        0.0232416,
        0.0197251,
        0.0217319,
        0.0198108,
        0.0193,
        0.0276144,
        0.0205839,
        0.026915,
        0.0312739,
        0.0415054,
        0.0740561,
        0.0598311,
        0.0598311 * 2.
    };
    int i_bin = 0;
    while (pt < ptmax[i_bin]) {
        ++i_bin;
    }
    return SFb_error[i_bin];
}


float BTagWeight::scaleFactorUDSG_CSVM(const float pt, const float eta)
{
    if (abs(eta) < 0.8) {
        if (pt > ptmax_16_) return sf_gt_ptmax_08_;
        return SFlight08_->Eval(pt);
    }

    if (abs(eta) < 1.6) {
        if (pt > ptmax_16_) return sf_gt_ptmax_16_;
        return SFlight16_->Eval(pt);
    }

    if (pt > ptmax_24_) return sf_gt_ptmax_24_;
    return SFlight24_->Eval(pt);
}


float BTagWeight::scaleFactor_CSVM(const pat::Jet& jet)
{
    partonFlavour_->Fill(jet.partonFlavour());
    switch (abs(jet.partonFlavour())) {
        case 5: return scaleFactorB_CSVM(jet.pt());
        case 4: return scaleFactorC_CSVM(jet.pt());
        default: return scaleFactorUDSG_CSVM(jet.pt(), jet.eta());
    }
}


float BTagWeight::weightBin0(const std::vector<float> &btagSFs)
{
    // product over i of (1 - btagSFs[i])
    float weight = 1.;
    for (unsigned i = 0; i < btagSFs.size(); ++i) {
        weight *= (1 - btagSFs[i]);
    }
    return weight;
}


float BTagWeight::weightBin1(const std::vector<float> &btagSFs)
{
    // sum over weight_i
    // where weight_i is
    // the product over not_i of (1 - btagSFs[not_i]) * btagSFs[i]
    float weight_sum = 0.;
    for (unsigned i_tagged = 0; i_tagged < btagSFs.size(); ++i_tagged) {
        float weight_i = 1.;
        for (unsigned i = 0; i < btagSFs.size(); ++i) {
            if (i_tagged == i) {
                weight_i *= btagSFs[i];
            } else {
                weight_i *= (1 - btagSFs[i]);
            }
        }
        weight_sum += weight_i;
    }
    return weight_sum;
}


float BTagWeight::bTagWeight(const std::vector<float> &btagSFs)
{
    float weight = 1.;
    weight -= weightBin0(btagSFs);
    if (twoBTagMode_)
        weight -= weightBin1(btagSFs);
    return weight;
}


// ------------ method called to produce the data  ------------
void
BTagWeight::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    double newEventWeight = 1.;

    // calculate event weight
    edm::Handle<std::vector<pat::Jet> > src;
    iEvent.getByLabel(src_, src);
    std::vector<float> btagSFs;
    std::vector<pat::Jet>::const_iterator jets = src->begin();
    for (; jets != src->end(); ++jets) {
        btagSFs.push_back(scaleFactor_CSVM(*jets));
    }
    newEventWeight *= bTagWeight(btagSFs);

    // if chained to prior weight function
    if (!emptyWeightInputTag_) {
        float weight = 1.;
        edm::Handle<double> weightHandle;
        iEvent.getByLabel(weights_, weightHandle);
        weight = *weightHandle.product();
        if (isnan(weight)) {
            weight = 1.;
        }
        newEventWeight *= weight;
    }

    // store in event
    std::auto_ptr<double> eventWeightOut(new double);
    *eventWeightOut = newEventWeight;
    iEvent.put(eventWeightOut);
}

// ------------ method called once each job just before starting event loop  ------------
void 
BTagWeight::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
BTagWeight::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
BTagWeight::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
BTagWeight::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
BTagWeight::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
BTagWeight::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
BTagWeight::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}




//define this as a plug-in
DEFINE_FWK_MODULE(BTagWeight);