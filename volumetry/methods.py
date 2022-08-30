"""Module contains methods for measuring kidney volume."""

import numpy as np
import SimpleITK as sitk


def voxels_volume(sitk_image, seg_slices):
    voxels = 0
    voxel_volume = 1

    for spacing in sitk_image.GetSpacing():
        voxel_volume *= spacing

    for seg_slice in seg_slices:
        # 1 stands for kindey
        values, counts = np.unique(seg_slice, return_counts=True)
        val_dict = dict(zip(values, counts))
        
        try:
            voxels +=  val_dict[1]
        except KeyError:
            pass
    
    volume = voxels * voxel_volume
    return volume
