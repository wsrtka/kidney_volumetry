"""Module containing utility functions."""

import SimpleITK as sitk


def divide_image(image):
    arr = sitk.GetArrayFromImage(image)
    half = arr.shape[2] // 2
    left_part = arr[:,:,:half]
    right_part = arr[:,:,half:]
    return left_part, right_part
