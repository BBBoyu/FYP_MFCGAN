import os
import numpy as np
from skimage import io, img_as_float, img_as_ubyte
from skimage.restoration import denoise_nl_means, estimate_sigma

# Specify the folder paths
input_folder = 'noisy_images_4'
output_folder = 'denoised_images'
os.makedirs(output_folder, exist_ok=True)

# Get a list of all images in the input folder
image_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.png')])

# Process each image (assuming you only want the first 14 images)
num_images = min(14, len(image_files))
for i in range(num_images):
    # Load the noisy image and convert to floating point format
    img = img_as_float(io.imread(os.path.join(input_folder, image_files[i]), as_gray=True))
    
    # Estimate noise standard deviation from the image
    sigma_est = np.mean(estimate_sigma(img))

    # Apply Non-Local Means filtering
    denoised_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True, 
                                    patch_size=5, patch_distance=6)
    
    # Convert back to 8-bit and save
    denoised_img = img_as_ubyte(denoised_img)
    output_filename = os.path.join(output_folder, f"denoised_{image_files[i]}")
    io.imsave(output_filename, denoised_img)
    print(f"Denoised image saved: {output_filename}")
