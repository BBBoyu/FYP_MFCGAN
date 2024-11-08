import os

# Specify the folder containing the images
folder_path = "DnCNN_denoised"

# Get a list of all files in the folder
files = sorted(os.listdir(folder_path))

# Loop through each file and rename it
for i, filename in enumerate(files):
    # Create the new filename (e.g., "image_1.png", "image_2.png", etc.)
    new_name = f"image_{i + 1}{os.path.splitext(filename)[1]}"  # Preserve the original file extension

    # Full paths for the old and new filenames
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_name)

    # Rename the file
    os.rename(old_file, new_file)
    print(f"Renamed '{filename}' to '{new_name}'")

print("All images have been renamed.")
