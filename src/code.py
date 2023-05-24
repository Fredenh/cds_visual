# Importing necessary packages 
import cv2
import os
import pandas as pd 
from PIL import Image
import numpy as np
import argparse
import tarfile

# Tool to unzip the data from .tgz 
tgz_path = os.path.join(".", "data", "17flowers.tgz")
zip_destination = os.path.join(".", "data")

with tarfile.open(tgz_path, 'r:gz') as tar:
    tar.extractall(path=zip_destination)

# Creating a function that finds the colour histogram of a selected image
def extract_color_histogram(image_path):
    # Accessing image with help from PIL since cv2.imread was problematic for my operating system
    image = Image.open(image_path) 
    # Converting to RGB 
    image = image.convert("RGB") 
    # Converting image to NumPy array
    image_np = np.array(image)
    # Calculating the colour histogram using openCV's cv2.calcHist method
    col_histogram = cv2.calcHist([cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    # Normalizing the colour histogram using openCV's cv2.normalize method
    histogram = cv2.normalize(col_histogram, col_histogram, 0, 1.0, cv2.NORM_MINMAX)

    return histogram

# Defining a function that finds the 5 images with the closest colour histogram to the chosen image
def find_5_images(chosen_image_path, folder_path):
    # Firstly, finding the colour histogram of the chosen image for later comparison
    chosen_hist = extract_color_histogram(chosen_image_path)
    # Making empty dictionary to store colour histograms of other images
    other_histograms = {}
    # Iterating through files in the "flowers" folder
    for file_name in os.listdir(folder_path):
       # Checks if it is a file and has a .jpg extension. To get around the problem of the .txt files in the "jpg" folder
        if not os.path.isfile(os.path.join(folder_path, file_name)) or not file_name.lower().endswith('.jpg'):
            continue
        # For files in the folder
        image_path = os.path.join(folder_path, file_name)
        # Open the image, again using PIL
        image = Image.open(image_path)
        # Converting every image to RGB 
        image = image.convert("RGB")
        # Converting every image into NumPy array
        image_np = np.array(image)
        # Converting from RGB to BGR using openCV's cv2.COLOR
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        # Extracting the colour histogram of images using the function defined earlier 
        other_histogram = extract_color_histogram(image_path)
        # Storing the histograms in the dictionary from before with the file_name as key
        other_histograms[file_name] = other_histogram
    
    # Creating empty list
    distances = []
    # The next section compares histograms with the histogram of the chosen image
    for file_name, other_histogram in other_histograms.items():
        # Here the histograms are compared via cv2.compareHist and rounded to two decimals 
        distance = round(cv2.compareHist(chosen_hist, other_histogram, cv2.HISTCMP_CHISQR), 2)
        # Appending the compared colour histograms to the distances list
        distances.append((file_name, distance))

    # Sorting the distances in ascending order based on the second element, which in this case is the distance metric scores
    distances.sort(key=lambda x: x[1])  
    # Making a new object with the chosen image and the 5 most similar images and their distance. 6 due to Pythons 0-based indexing
    top_five = distances[:6]
    # Creating a Pandas dataframe from the top 5 closest images and their distance
    df = pd.DataFrame(top_five, columns=["Filename", "Distance"])

    # Specifying the outpath
    outpath = os.path.join(".", "out")
    # Defining the name of the output 
    csv_name = "top_five.csv"
    # Saving the dataframe as a CSV file. Index set to False in order to avoid the index column in the output
    df.to_csv(os.path.join(outpath, csv_name), index=False)

# The main function that runs the code
def main(args):
    # Here i specify the location of the folder where the images are located
    folder_path = os.path.join(".", "data", "jpg")
    # This section checks if there is provided a target image as an argument when the script is run from the command line
    if args.target_image is None:
        # If it is not the case, the default image is "image_1342.jpg"
        chosen_image_name = "image_1342.jpg"
    else:
        chosen_image_name = args.target_image
    # Creating the full path to the chosen image 
    chosen_image_path = os.path.join(folder_path, chosen_image_name)
    # Using function created above to find the 5 most similar colour histograms
    find_5_images(chosen_image_path, folder_path)

if __name__ == "__main__":
    # Creating the arugment parser
    parser = argparse.ArgumentParser()
    # Here i add a positional string argument for the image "target_image". "nargs" makes the argument optional, whereas the "default=None" specifies the default if an argument is not provided  
    parser.add_argument("target_image", type=str, nargs='?', default=None)
    # Parsing the command line argument 
    args = parser.parse_args()
    # Calling the main function with args as argument
    main(args)
