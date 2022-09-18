"""Module containing utility functions."""

import numpy as np
import SimpleITK as sitk


def divide_image(image):
    arr = sitk.GetArrayFromImage(image)
    half = arr.shape[2] // 2
    left_part = arr[:,:,:half]
    right_part = arr[:,:,half:]
    return left_part, right_part

def find_kidney_slices(segmentation, seg_val=1):
    max_idx = None
    first_idx = segmentation.shape[2]
    last_idx = 0
    max_counts = 0

    for idx, seg_slice in enumerate(segmentation):
        mask = seg_slice == seg_val
        _, counts = np.unique(mask, return_counts=True)
        if len(counts) > 1:
            if counts[1] > max_counts:
                max_counts = counts[1]
                max_idx = idx
            if idx < first_idx:
                first_idx = idx
            if idx > max_idx:
                last_idx = idx

    return first_idx, last_idx, max_idx
