from PIL import Image
import os

# Define the input and output directories
input_folder = 'frames'
output_folder = 'frames_resized_gray'  # change if you want a separate output folder

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # Open, resize, and convert the image to grayscale
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            img_resized_gray = img.resize((64, 64)).convert('L')  # Resize and convert to grayscale
            # Save the resized grayscale image to the output folder
            img_resized_gray.save(os.path.join(output_folder, filename))
        print(f"Resized, converted to grayscale, and saved {filename}")

print("All images have been resized and converted to grayscale.")
