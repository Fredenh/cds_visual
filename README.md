[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10361132&assignment_repo_type=AssignmentRepo)

# Assignment 1 - Simple image search algorithm 
This is the first of four assignments for the Visual Analytics course

# Contribution
The assignment was initially done in collaboration with other course participants. The final version of the code was developed independently by me. I have also made several modifications to the code since the initial submission. 

# Ross' instructions

For this assignment, you'll be using ```OpenCV``` to design a simple image search algorithm.

The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/).

For this exercise, you should write some code which does the following:

- Define a particular image that you want to work with
- For that image
  - Extract the colour histogram using ```OpenCV```
- Extract colour histograms for all of the **other* images in the data
- Compare the histogram of our chosen image to all of the other histograms 
  - For this, use the ```cv2.compareHist()``` function with the ```cv2.HISTCMP_CHISQR``` metric
- Find the five images which are most simlar to the target image
  - Save a CSV file to the folder called ```out```, showing the five most similar images and the distance metric:

|Filename|Distance]
|---|---|
|target|0.0|
|filename1|---|
|filename2|---|

Bonus task: 


# Methods
For the main task, the code.py script finds the 5 most similar images to a selected target image identified by myself. Firstly, a normalised colour histogram is created for the target image. It is then compared to the colour histograms of all the other images in the data folder. The script does this by looping over all the images, creating a normalised colour histogram for each image and then comparing them with that of the target image. It then identifies the 5 most similar colour histograms and saves a csv to the "out" folder with the distance metric score and the name of the five images.

For the bonus task 

# Usage 
To run the script, you first need to install the necessary packages. To do this navigate to the "assignment1" folder and run the following from the command line:

bash setup.sh

Within the "setup.sh" file there is a command to install the packages listed in the "requirements.txt" file.

Get the data

The data orignially stems from the following link:

https://www.robots.ox.ac.uk/~vgg/data/flowers/17/

However, for the assignment, the class was provided with a zip file containing the dataset. 
The data is located in a zip file within the "in" folder. To unzip the zip file and get access to all the images contained within run the following commands in the command line:

python -c "import zipfile; zipfile.ZipFile('path/to/your/file.zip', 'r').extractall('in')"

To run the main task make sure to navigate to the "assignment1" folder. Then run the following from the command line:

python3 src/code.py 

After running the script the results are located in the "out" folder as "top_five.csv"

## Discussion of results

