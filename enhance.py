from PIL import Image, ImageEnhance
import os

image_folder = input("Enter the path to the images folder: ")
output_folder = input("Enter the path to the output images folder: ")
image_files = []

#get image files in the folder
for filename in os.listdir(image_folder):
    if not filename.startswith('.') and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_files.append(filename)

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

for img in image_files:
    input_path = image_folder + '/' + img
    output_path = output_folder + '/' + img

    def enhance_image(input_path, output_path):
        # Open the image using Pillow
        image = Image.open(input_path)

        # Enhance the image using Pillow's ImageEnhance module
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(1.2)  # Increase contrast
        enhanced_image = ImageEnhance.Brightness(enhanced_image).enhance(1.1)  # Increase brightness

        # Save the enhanced image
        enhanced_image.save(output_path)

    enhance_image(input_path, output_path)

    print(f"Processed: {img} => {output_path}")
    
print("Processing complete.")