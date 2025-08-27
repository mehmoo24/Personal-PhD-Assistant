# Adapted from Dan's script: https://cdcvs.fnal.gov/cgi-bin/public-cvs/cvsweb-public.cgi/AnalysisFramework/Ana/CCQENuInclusiveME/ana/plot_macros_pub/CrossSections/NEUT/PlotInclusive.py?annotate=1.2;cvsroot=mnvsoft

import ROOT
import array
import sys
import ROOT.TFile
import ROOT.TTree
#import TFile::Init

def getMuonMomentum(mytree, lep_pdg_want):
   muon_mom = ROOT.TVector3()

   nfsp = mytree.nfsp
   Efsp = mytree.E
   pdg = mytree.pdg
   px = mytree.px
   py = mytree.py
   pz = mytree.pz

   for p in range(0,nfsp):
      if(pdg[p]==lep_pdg_want):
         muon_mom.SetX(px[p])
         muon_mom.SetY(py[p])
         muon_mom.SetZ(pz[p])
         break
   return muon_mom

def isInclusive(mytree, nu_pdg_want, lep_pdg_want):
   nu_pdg = mytree.PDGnu
   lep_pdg = mytree.PDGLep
   cc = mytree.cc   

   if(nu_pdg == nu_pdg_want and lep_pdg == lep_pdg_want):
#   if(nu_pdg == 14 and cc == 1):
      return True

   return False

def isGoodMuon(mytree, lep_pdg_want):
   # <20 degree muon
   # 1.5 to 60 muon mom
   muonmom = getMuonMomentum(mytree, lep_pdg_want)
#   goodMuonMom   = muonmom.Mag()>1.5 and muonmom.Mag()<60
   goodMuonAngle = muonmom.Theta()*180/3.1415 < 20

   if goodMuonAngle: return True
#   if goodMuonMom and goodMuonAngle: return True
 
   return False


nu_pdg_want=int(sys.argv[1])
lep_pdg_want=int(sys.argv[2])
inputFile=ROOT.TFile(sys.argv[3])
outputFile_name=sys.argv[4]
flag_useLownu = bool(int(sys.argv[5])) # 0 is false, 1 is true

print("Neutrino PDG:", nu_pdg_want)
print("Lepton PDG:", lep_pdg_want)
print("Output file:", outputFile_name)
print("Run Low-ν?", flag_useLownu)

mytree = inputFile.Get("FlatTree_VARS")

ptbins = [0,0.07,0.15,0.25,0.33,0.4,0.47,0.55,0.7,0.85,1,1.25,1.5,2.5,4.5]
pzbins = [1.5,2.,2.5,3.,3.5,4.,4.5,5.,6.,7.0,8.,9.0,10.,15.,20.,40.,60.]

myptpz = ROOT.TH2D("ptpz","ptpz",len(pzbins)-1, array.array("d",pzbins),len(ptbins)-1,array.array("d",ptbins))

for e in mytree:
   if not (isInclusive(e, nu_pdg_want, lep_pdg_want) and isGoodMuon(e, lep_pdg_want)): continue
   coslep = e.CosLep
   elep= e.ELep
   fScaleFactor = e.fScaleFactor

   P = ROOT.TMath.Sqrt(elep*elep-0.105*0.105)
   Pl = coslep*P
   Pt = ROOT.TMath.Sqrt(1-coslep*coslep)*P

   myptpz.Fill(Pl,Pt,fScaleFactor)

myptpz.GetXaxis().SetTitle("Muon p_{||} (GeV)")
myptpz.GetYaxis().SetTitle("Muon p_{t} (GeV)")

myoutput = ROOT.TFile(outputFile_name,"RECREATE")
myptpz.Write();
