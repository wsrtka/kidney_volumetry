"""Module contains methods for measuring kidney volume."""

import numpy as np
import SimpleITK as sitk

from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter


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

def ellipsoid_method(max_seg, first_idx, last_idx):
    edges = canny(max_seg)

    ellipses = hough_ellipse(edges, min_size=35)
    ellipses.sort(order='accumulator')
    param = list(ellipses[-1])

    yc, xc, a, b = [int(round(x)) for x in param[1:5]]
    orientation = param[5]
    xs, ys = ellipse_perimeter(yc, xc, a, b, orientation)

    c = last_idx - first_idx
    volume = a * b * c * np.pi * (2 / 3)
    
    return volume, xs, ys
