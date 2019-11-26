In this project, I tried to do fMRI analysis using python.

Main.py uses the 'fmri.glm.FMRILinearModel' function from NIPY.

This function requires 3 inputs: fmri_files (run.nii files), desing_files (computed by design_matrix_generator.py) and mask (computed by mask_generator.py)

Data from Openneuro:
https://openneuro.org/datasets/ds000005/versions/00001
Tom, S.M., Fox, C.R., Trepel, C., Poldrack, R.A. (2007). The neural basis of loss aversion in decision-making under risk. Science, 315(5811):515-8

Although the code is working without format errors, the analysis unfortunately is not correct (no preprocessing, not the correct analysis for the design of the study)
