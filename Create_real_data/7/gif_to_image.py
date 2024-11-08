from PIL import Image
import os

# Define the path to your GIF file and the directory to save frames
gif_path = 'mri_image.gif'
output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

# Open the GIF
with Image.open(gif_path) as img:
    # Ensure the file is an animated GIF
    if img.is_animated:
        # Loop through each frame (up to 14 frames)
        for frame in range(14):
            # Set the GIF to the correct frame
            img.seek(frame)
            # Save the frame as a separate image
            frame_path = os.path.join(output_dir, f'frame_{frame:02d}.png')
            img.save(frame_path, format='PNG')
            print(f'Saved {frame_path}')
    else:
        print("This GIF does not have multiple frames.")
