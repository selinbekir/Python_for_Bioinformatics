#!/usr/bin/env python


import matplotlib.pyplot as plt
import nibabel as nib
# from png_to_array import *

import sys

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise RuntimeError("This script needs the matplotlib library")

from nipy.labs.viz import plot_map, cm
from nipy.modalities.fmri.glm import FMRILinearModel

import argparse
from os import listdir
from os.path import isfile, join
import main.mask_generator as mask_generator
import main.design_matrix_generator as design_matrix_generator


cvect = [1, 0, 0, 0]

# todo get patient by arg parser(run1, run2, run3)

# todo create mask file

# todo create design files [design1, design2, ..]

# todo run files [run1, run2, ..]


# Instantiate the parser
parser = argparse.ArgumentParser(description='Please provide a patient directory path')
# Required patient argument
parser.add_argument('path',
                    help='Patient Path Directory')
args = parser.parse_args()

if args.path is None:
    parser.error("Directory Path should be added as argument")

fmri_files = [f for f in listdir(args.path) if isfile(join(args.path, f))]
mask_file = mask_generator.make_mask(args.path, "./Group_Mask")
design_files = design_matrix_generator.make_design(args.path)

multi_session_model = FMRILinearModel(fmri_files, design_files, mask_file)

# GLM fitting
multi_session_model.fit(do_scaling=True, model='ar1')

# Compute the required contrast
print('Computing test contrast image...')
n_regressors = [np.load(f)['arr_0'].shape[1] for f in design_files]
con = [np.hstack((cvect, np.zeros(nr - len(cvect)))) for nr in n_regressors]
z_map, = multi_session_model.contrast(con)

# Show Z-map image
mean_map = multi_session_model.means[0]

print(mean_map)
plot_map(z_map.get_data(),
         z_map.get_affine(),
         anat=mean_map.get_data(),
         anat_affine=mean_map.get_affine(),
         cmap=cm.cold_hot,
         threshold=2.5,
         black_bg=True)

plt.savefig('1st_analiz.png')
