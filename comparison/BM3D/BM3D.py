import cv2
import numpy as np
from bm3d import bm3d
import glob
import os

# Define paths
input_folder = "noisy_images_4"
output_folder = "denoised_images"
os.makedirs(output_folder, exist_ok=True)

# Load all image paths
image_paths = sorted(glob.glob(os.path.join(input_folder, "*.png")))

# Select every 20th image to get each unique frame
unique_image_paths = image_paths[::20]

# Define noise level for BM3D
sigma_psd = 0.1 # Adjust based on the noise level

# Process each unique image
for i, image_path in enumerate(unique_image_paths):
    # Load the image in grayscale mode
    noisy_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the image to 64x64
    noisy_image = cv2.resize(noisy_image, (64, 64))
    
    # Ensure the image is in float format (required by bm3d)
    noisy_image = noisy_image.astype(np.float32) / 255.0
    
    # Apply BM3D denoising
    denoised_image = bm3d(noisy_image, sigma_psd)
    
    # Convert the denoised image back to 8-bit format
    denoised_image = (denoised_image * 255).astype(np.uint8)
    
    # Save the denoised image
    output_path = os.path.join(output_folder, f"denoised_frame_{i+1}.png")
    cv2.imwrite(output_path, denoised_image)
    print(f"Denoised image saved at {output_path}")
