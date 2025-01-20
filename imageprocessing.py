# Importando bibliotecas necessárias
import os
import numpy as np
import platform
from tkinter.filedialog import askdirectory
from PIL import Image

# Function to create the output folders
def folder_create(folder_path):
    # Get the parent directory and the original folder name
    parent_dir, original_folder = os.path.split(folder_path)
    
    # Create the new base folder named "{original folder} processed"
    processed_base = os.path.join(parent_dir, f"{original_folder} processed")
    
    # Create paths for the subfolders
    gray_path = os.path.join(processed_base, "Grayscale")
    bw_path = os.path.join(processed_base, "B&W")

    #check if the folders already exists and then create them if not
    if os.path.exists(gray_path) == False:
        os.makedirs(gray_path)
    if os.path.exists(bw_path) == False:
        os.makedirs(bw_path)
    
    return processed_base

#Function to read the folder files
def get_image_files(folder_path):
    valid_extensions = (".jpg", "jpeg",".png",".bmp",".tiff",".JPG")
    image_files = [] #empty list to store all valid image files
    with os.scandir(folder_path) as it:
        for entry in it:
            if entry.is_file() and entry.name.lower().endswith(valid_extensions):
                image_files.append(entry.path) #add the full path of the image
    return image_files #return the storage

#function to process each image
def image_process(input_image_path, output_folder):
    # Step 1: Open the image with Pillow
    img = Image.open(input_image_path)
    pixels = np.array(img)

    # Step 2: Convert to grayscale
    grayscale_pixels = (0.3 * pixels[:, :, 0] + 0.59 * pixels[:, :, 1] + 0.11 * pixels[:, :, 2]).astype(np.uint8)

    # Step 3: Save the grayscale image
    grayscale_img = Image.fromarray(grayscale_pixels, mode="L")
    output_image_path = os.path.join(output_folder, os.path.basename(input_image_path))
    grayscale_img.save(output_image_path)

#function to binarize the image
def binarize_image(input_image_path, output_folder, threshold=128):
    #step 1: open the grayscale image
    img = Image.open(input_image_path).convert("L") #ensure it's grayscale

    #step 2: apply binarization
    binary_img = img.point(lambda p: 255 if p >= threshold else 0)

    #step 3: save the binary image
    output_image_path = os.path.join(output_folder, os.path.basename(input_image_path))
    binary_img.save(output_image_path)

def open_folder(folder_path):
    """
    Open the folder in the default file explorer.
    """
    if platform.system() == "Windows":  # For Windows
        os.startfile(folder_path)
    elif platform.system() == "Darwin":  # For macOS
        os.system(f"open {folder_path}")
    elif platform.system() == "Linux":  # For Linux
        os.system(f"xdg-open {folder_path}")

#main program
print("Please select the folder with the images.")
folder_path = askdirectory()

if folder_path: #check if a folder was selected
    #use folder creation func
    processed_base = folder_create(folder_path)

    #use image getting func
    image_files = get_image_files(folder_path)
    print(f"Found {len(image_files)} image(s):")

    #process images  
    for img in image_files:
        print(f"processing {img}...")

        #convert to grayscale
        grayscale_folder = os.path.join(processed_base, "Grayscale")
        image_process(img, grayscale_folder)
        print(f"Saved grayscale version of {os.path.basename(img)}.")

        #convert to binary
        binary_folder = os.path.join(processed_base, "B&W")
        binarize_image(os.path.join(grayscale_folder, os.path.basename(img)), binary_folder)

        print(f"Processed {os.path.basename(img)}.")
        
    #open the folder after done with the images
    open_folder(processed_base)
    print("All images processed. Folder opened!")

else:
    print("No folder was selected.")