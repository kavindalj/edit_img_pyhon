from PIL import Image, ImageEnhance
import os

image_folder = 'FOLDER PATH FOR IMAGES'
output_flder = 'FOLDER PATH FOR EDITED IMAGES'
image_files = []

#get image files in the folder
for filename in os.listdir(image_folder):
    if not filename.startswith('.') and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_files.append(filename)


for img in image_files:
    global input_path
    global output_path
    input_path = image_folder + '/' + img
    output_path = output_flder + '/' + img

    def crop_and_enhance_image(input_path, output_path):
        # Open the image using Pillow
        image = Image.open(input_path)

        # Calculate the desired width and height for 1.1 aspect ratio
        aspect_ratio = 1.1
        width, height = image.size
        new_width = min(int(height * aspect_ratio), width)
        new_height = min(int(new_width / aspect_ratio), height)

        # Calculate cropping coordinates for centered crop
        x_start = max(0, (width - new_width) // 2)
        y_start = max(0, (height - new_height) // 2)

        # Perform the crop
        cropped_image = image.crop((x_start, y_start, x_start + new_width, y_start + new_height))

        # Enhance the image using Pillow's ImageEnhance module
        enhancer = ImageEnhance.Contrast(cropped_image)
        enhanced_image = enhancer.enhance(1.2)  # Increase contrast
        enhanced_image = ImageEnhance.Brightness(enhanced_image).enhance(1)  # Increase brightness

        # Save the enhanced image
        enhanced_image.save(output_path)

    crop_and_enhance_image(input_path, output_path)