import os, subprocess
folder = "error"
filelist = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

for ifile in filelist:
    line = subprocess.check_output(['tail', '-2', os.path.join(folder,ifile)])
    if line.strip() != "TFile::Append:0: RuntimeWarning: Replacing existing TH1: h_total_mcweight (Potential memory leak).":
        n=2
        while line.strip() == "":
            n+=1
            line = subprocess.check_output(['tail', '-'+str(n), os.path.join(folder,ifile)])
        line = subprocess.check_output(['tail', '-'+str(n+1), os.path.join(folder,ifile)])   
        print ifile+" :"
        print line
        print
        
