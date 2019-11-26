import os
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
from nipy.modalities.fmri.design_matrix import make_dmtx
import nibabel as nib
import json


def make_design(folder_name):
    files = [f for f in listdir(folder_name) if isfile(join(folder_name, f))]
    design_files = []
    for i, run_file in files:
        name = "design-{}".format(i)
        tr = 0.2
        path = os.path.join(folder_name, run_file)
        img = nib.load(path)
        data = img.get_data()
        n_scans = data.shape[-1]
        frametimes = np.arange(0, n_scans * tr, tr)
        y = make_dmtx(frametimes, paradigm=None, hrf_model='canonical', drift_model='cosine',
                      hfcut=128, drift_order=1, fir_delays=[0],
                      add_regs=None, add_reg_names=None, min_onset=0)

        np.savez(name, y.matrix)
        design_files.append(name)

    return design_files
