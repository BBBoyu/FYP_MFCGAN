import os
from PIL import Image
import matplotlib.pyplot as plt

# Define paths to your folders
folders = {
    "Noisy": "noisy",
    "Ground Truth": "ground_truth",
    "BM3D_denoised": "BM3D_denoised",
    "NLM_denoised": "NLM_denoised",
    "DnCNN_denoised": "DnCNN_denoised",
    "CycleGAN_denoised": "cyclegan_denoised",
    "MFCGAN_denoised": "MFCGAN_denoised"
}

# Specify the image you want to compare (e.g., "image_1.png")
image_name = "image_1.png"

# Create a plot to show one image from each folder
fig, axes = plt.subplots(1, len(folders), figsize=(15, 5))
fig.suptitle(f"Comparison of Denoising Methods", fontsize=16)

for ax, (method_name, folder_path) in zip(axes, folders.items()):
    # Load the image from the corresponding folder
    image_path = os.path.join(folder_path, image_name)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        ax.imshow(image, cmap='gray')
        ax.set_title(method_name)
    else:
        ax.text(0.5, 0.5, 'Image not found', ha='center', va='center', fontsize=12, color='red')
    
    ax.axis('off')

fig.tight_layout()
plt.show()
