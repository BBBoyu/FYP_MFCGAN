import os
import pandas as pd
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim
import numpy as np
import dataframe_image as dfi  # Required to save DataFrame as an image

# Define paths to folders for each method
folders = {
    "Noisy": "noisy",
    "Ground Truth": "ground_truth",
    "BM3D_denoised": "BM3D_denoised",
    "NLM_denoised": "NLM_denoised",
    "DnCNN_denoised": "DnCNN_denoised",
    "CycleGAN_denoised": "cyclegan_denoised",
    "MFCGAN_denoised": "MFCGAN_denoised"
}

# Initialize a dictionary to store PSNR and SSIM scores for each method
method_scores = {method: {"PSNR": [], "SSIM": []} for method in folders if method != "Ground Truth"}

# Get list of ground truth images (assuming all folders have matching images)
ground_truth_files = sorted(os.listdir(folders["Ground Truth"]))

# Loop through each ground truth image and calculate scores for corresponding images in each method folder
for gt_image_name in ground_truth_files:
    # Load the ground truth image
    gt_image_path = os.path.join(folders["Ground Truth"], gt_image_name)
    ground_truth_image = np.array(Image.open(gt_image_path).convert("L"))

    # For each denoising method, calculate PSNR and SSIM with the ground truth
    for method_name, folder_path in folders.items():
        if method_name == "Ground Truth":
            continue  # Skip the ground truth folder for comparisons

        # Path to the corresponding image in the current method's folder
        method_image_path = os.path.join(folder_path, gt_image_name)
        
        # Check if the corresponding image exists in the method folder
        if os.path.exists(method_image_path):
            # Load the method's image
            method_image = np.array(Image.open(method_image_path).convert("L"))
            
            # Compute PSNR and SSIM between the method image and ground truth
            psnr_value = psnr(ground_truth_image, method_image, data_range=method_image.max() - method_image.min())
            ssim_value = ssim(ground_truth_image, method_image, data_range=method_image.max() - method_image.min())
            
            # Append the scores to the respective lists
            method_scores[method_name]["PSNR"].append(psnr_value)
            method_scores[method_name]["SSIM"].append(ssim_value)
        else:
            print(f"Warning: {gt_image_name} not found in {method_name} folder")

# Calculate the average PSNR and SSIM for each method
average_scores = {"Method": [], "Average PSNR": [], "Average SSIM": []}
for method, scores in method_scores.items():
    average_psnr = np.mean(scores["PSNR"]) if scores["PSNR"] else 0
    average_ssim = np.mean(scores["SSIM"]) if scores["SSIM"] else 0
    average_scores["Method"].append(method)
    average_scores["Average PSNR"].append(average_psnr)
    average_scores["Average SSIM"].append(average_ssim)

# Convert to DataFrame for easy viewing
results_df = pd.DataFrame(average_scores)

# Format and save the table as an image
df_styled = results_df.style.format({"Average PSNR": "{:.2f}", "Average SSIM": "{:.2f}"}).set_caption("Average PSNR and SSIM Scores for Denoising Methods")
dfi.export(df_styled, "average_denoising_scores_table.png")

# Display the average scores as a formatted table for quick review
print(results_df)

