from PIL import Image
import os

# Paths for input and output folders
background_folder = input("Enter the path to the images folder: ")  # Folder containing background images
output_folder = input("Enter the path to the output images folder: ")    # Folder to save the resulting images

# Load the overlay image
overlay_image = Image.open("/Users/kavinda/Documents/projects/self-studies/python/img edit/logo.png")

# Get a list of background image files
background_image_files = [file for file in os.listdir(background_folder) if not file.startswith('.') and file.lower().endswith((".png", ".jpg", ".jpeg"))]

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each background image
for background_image_file in background_image_files:
    # Load the background image
    background_image = Image.open(os.path.join(background_folder, background_image_file))
    
    # Resize the overlay image to match the background image's dimensions
    overlay_image_resized = overlay_image.resize(background_image.size)
    
    # Overlay the images
    position = (0, 0)  # Define the position where you want to place the overlay image
    result_image = background_image.copy()
    result_image.paste(overlay_image_resized, position, overlay_image_resized)
    
    # Save the resulting image to the output folder
    output_image_path = os.path.join(output_folder, background_image_file)
    result_image.save(output_image_path)

    print(f"Processed: {background_image_file} => {output_image_path}")

print("Processing complete.")
