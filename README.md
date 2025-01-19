# Image Processing Script

## **Description**
This Python script processes images by converting them into grayscale and binary (black-and-white) formats. The processed images are organized into structured output folders for easier management and use.

## **Features**
- Converts images from RGB (color) to grayscale.
- Applies binarization using a threshold to produce black-and-white images.
- Organizes output into structured folders within a new folder named after the original input folder.

## **Requirements**
Ensure you have the following installed:
- Python 3.7+
- Required libraries:
  - Pillow
  - NumPy

### Install the Required Libraries
Use the following commands to install the required libraries:
```bash
pip install pillow numpy
```

## **How to Use**
1. **Run the script**:
   - Execute the script using Python in your terminal or code editor.
```bash
python imageprocessing.py
```

2. **Select the input folder**:
   - A dialog box will open for you to select the folder containing the images to process.

3. **Processed images**:
   - The script will create a new folder named after the input folder with the suffix `processed`.
   - Inside this folder, two subfolders will be created:
     - `Grayscale`: Contains images converted to grayscale.
     - `B&W`: Contains images converted to black and white (binary).

## **Folder Structure**
The processed images will follow this structure:
```
/dataset
  /input_folder
    image1.jpg
    image2.jpg
  /input_folder processed
    /Grayscale
      image1.jpg
      image2.jpg
    /B&W
      image1.jpg
      image2.jpg
```

## **Adjusting Parameters**
- **Threshold for Binarization**:
  - The default threshold is `128`.
  - To modify it, adjust the `threshold` parameter in the `binarize_image` function:
    ```python
    binarize_image(input_image_path, output_folder, threshold=your_value)
    ```

## **Example Execution**
1. **Input Folder:**
   - `/dataset/images`

2. **Output Folder:**
   - `/dataset/images processadas`
     - `/Grayscale`
     - `/B&W`

3. **Output Example:**
   - Grayscale and binarized versions of all images will appear in the respective subfolders.

## Next Updates:

The next update will focus on creating a standalone executable (.exe) and a user interface to make the script more user-friendly and eliminate the need for Python or additional libraries.

## **Author**
- João Augusto 

Feel free to enhance or adapt this script for your needs! 🚀
Your feedback will always be important for my learning.