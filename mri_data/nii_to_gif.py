import nibabel as nib
import imageio
import numpy as np

# Load the NIfTI file
img = nib.load('G2O2S6_sa.nii')
data = img.get_fdata()

# Define whether it's 3D or 4D
is_4d = data.ndim == 4

# Choose an axis and slice. For example, we'll use the middle slice along the Z-axis.
slice_index = data.shape[2] // 2  # Use the middle slice for 3D structure

# Prepare frames for GIF
frames = []

# If it's 4D (time series), iterate over the time dimension
if is_4d:
    for t in range(data.shape[3]):  # Iterate through time
        # Extract a single 2D slice at the current time point
        slice_2d = data[:, :, slice_index, t]
        # Normalize for visualization
        slice_2d = (slice_2d - np.min(slice_2d)) / (np.max(slice_2d) - np.min(slice_2d)) * 255
        slice_2d = slice_2d.astype(np.uint8)
        frames.append(slice_2d)

else:
    # For 3D NIfTI files, iterate over the slices along an axis, e.g., Z-axis
    for z in range(data.shape[2]):
        slice_2d = data[:, :, z]
        slice_2d = (slice_2d - np.min(slice_2d)) / (np.max(slice_2d) - np.min(slice_2d)) * 255
        slice_2d = slice_2d.astype(np.uint8)
        frames.append(slice_2d)

# Save as GIF
imageio.mimsave('output7.gif', frames, duration=0.1)  # duration controls frame speed
