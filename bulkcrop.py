import os
from Katna.image import Image
from Katna.writer import ImageCropDiskWriter

img_module = Image()

image_folder = input("Enter the path to the images folder: ")
output_folder = input("Enter the path to the output images folder: ")
image_files = []

#get image files in the folder
for filename in os.listdir(image_folder):
    if not filename.startswith('.') and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_files.append(filename)

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# diskwriter to save crop data
diskwriter = ImageCropDiskWriter(location=output_folder)

for img in image_files:
    input_path = image_folder + '/' + img
    output_path = output_folder + '/' + img

    crop_list = img_module.crop_image_with_aspect(
    file_path=input_path,
    crop_aspect_ratio='1:1',
    num_of_crops=1,
    writer=diskwriter,
    filters="text",
    down_sample_factor=8
    )

    print(f"Processed: {img} => {output_path}")

print("Processing complete.")