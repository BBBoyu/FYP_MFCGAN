from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import numpy as np
import os
from PIL import Image

# Load ground truth and denoised images
ground_truth_folder = 'ground_truth/'
denoised_folder = 'cyclegan_denoised/'

ground_truth_files = sorted(os.listdir(ground_truth_folder))
denoised_files = sorted(os.listdir(denoised_folder))

# Store PSNR and SSIM values for each matched pair
psnr_values = []
ssim_values = []

for denoised_file in denoised_files:
    denoised_image = np.array(Image.open(os.path.join(denoised_folder, denoised_file)).convert('L'))
    best_ssim = -1
    best_psnr = -1
    best_gt_image = None

    # Find the ground truth image with the highest SSIM compared to the denoised image
    for ground_truth_file in ground_truth_files:
        ground_truth_image = np.array(Image.open(os.path.join(ground_truth_folder, ground_truth_file)).convert('L'))

        # Calculate SSIM and PSNR for this pair
        current_ssim = ssim(ground_truth_image, denoised_image, data_range=ground_truth_image.max() - ground_truth_image.min())
        current_psnr = psnr(ground_truth_image, denoised_image, data_range=ground_truth_image.max() - ground_truth_image.min())

        # Update best match based on SSIM
        if current_ssim > best_ssim:
            best_ssim = current_ssim
            best_psnr = current_psnr
            best_gt_image = ground_truth_file

    # Save best SSIM and PSNR values for this denoised image
    psnr_values.append(best_psnr)
    ssim_values.append(best_ssim)
    print(f"Matched {denoised_file} to {best_gt_image} with SSIM: {best_ssim:.4f} and PSNR: {best_psnr:.4f}")

# Calculate and display the average PSNR and SSIM
average_psnr = np.mean(psnr_values)
average_ssim = np.mean(ssim_values)

print("Average PSNR:", average_psnr)
print("Average SSIM:", average_ssim)
