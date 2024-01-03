from pyzbar.pyzbar import decode
from PIL import Image
import os

def extract_barcode_info(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    output_file = 'barcode_output.txt'
    with open(output_file, 'a') as file:
        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            barcode_type = obj.type
            file.write(f"File: {image_path}, Barcode Type: {barcode_type}, Data: {barcode_data}\n")

def extract_from_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            extract_barcode_info(image_path)

# Replace 'folder_path' with the directory path containing your images
folder_path = '.\\runs\\detect\\predict\\crops\\barcode'
extract_from_folder(folder_path)