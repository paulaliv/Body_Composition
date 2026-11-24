import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

# Paths
ct_path = r"C:\Users\paula\Downloads\SAROS_CT_IMAGES\case_000\image.nii.gz"
seg_path = r"SAROS-Collection-NIfTI-files-v2_03-70-2024/SAROS-Collection-NIfTI-files-v2_03-70-2024/case_000/body-regions.nii.gz"

# Load NIfTI files
ct_nii = nib.load(ct_path)
seg_nii = nib.load(seg_path)

# Get image arrays
ct = ct_nii.get_fdata()
seg = seg_nii.get_fdata()

print("CT shape:", ct.shape)
print("Segmentation shape:", seg.shape)

print("CT affine:\n", ct_nii.affine)
print("Seg affine:\n", seg_nii.affine)