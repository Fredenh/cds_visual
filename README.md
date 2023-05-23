[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10361132&assignment_repo_type=AssignmentRepo)

# Assignment 1 - Simple image search algorithm 
This is the first of four assignments for the Visual Analytics course

# Contribution
The assignment was initially done in collaboration with other course participants. Help was also gathered from the notebooks in class. The final version of the code was developed independently by me. I have also made several modifications to the code since the initial submission. 

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

# Data

The data for this assignment was originally created by [Maria-Elena Nilsback and Andrew Zisserman](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/) from the University of Oxford. The data i use is from a [Kaggle](https://www.kaggle.com/datasets/saidakbarp/17-category-flowers) user called Saidakbarp. Its a .tgz file that in total contains over 1300 images of different flowers.

# Packages 
I used a small variety of different packages for this assignment. I will in the following bulletpoints list them and for what purpose they were needed
* ```OpenCV``` is used to extract colour histograms and compare them with each other
* ```Pandas``` is used to convert the output to a dataframe 
* ```Pillow``` is used to open images. I only resorted to using ```Pillow``` because I encountered issues when transitioning between operating systems. ```OpenCV``` and its ```cv2.imread()``` method conflicted with my Windows 11 operating system during this assignment and i couldnt troubleshoot it.
* ```os``` is used to navigate paths.
* ```argparse``` is used to create command line arguments that gives the user of the script a choice of which image to compare with others.
* ```Numpy``` is used to convert into arrays
* ```tarfile``` to unzip the data 

# Methods
This script, code.py, starts by defining a function that extracts colour histograms of a given image. It does this by using ```OpenCV```'s ```calcHist``` method. After the colour histogram is calculated, the function then normalizes the image using ```normalize``` and the argument cv2.NORM_MINMAX. I have chosen to limit the pixel values between 0 and 1.0. Now, the function is utilized in another function that iterates through every image in the data, calculates colour histograms, normalizes and eventually compares them to the chosen image. The function uses ```compareHist``` from ```OpenCV``` with the argument cv2.HISTCMP_CHISQR which finds the distance metric score between the chosen image and all the other images. It sorts the colour histograms so that the 5 closest scores are identified. Then it creates a ```Pandas```dataframe and saves the output to a csv file in the _out_ folder

# Discussion of results
After consulting the output of my image search algorithm it is clear that this method of finding similarities gives a quick overview of distance in colour attributes. But for more in depth insight into similarities in images, feature extraction from a pretrained model would most certainly perform better. But for the sake of simplicity and less computational resources spent, the approach in this assignment is satisfactory for shallow results. With the standard image provided in the code, if one not chooses to argparse another image, the closest distance score is 635.98. It is hard to tell if this is close or not, but as i played around with it and parsed different images in the command line, i found that the standard image, although chosen randomly, has quite close neighbours. Because in some instances, the closest distance score was over 3000. The reason why these scores vary so much is because the background of the images also is counted into the overall colour histograms. 

# Usage 
* First you need to acquire the data from [Kaggle](https://www.kaggle.com/datasets/saidakbarp/17-category-flowers) and place it in the _data_ folder. 
* Then you run ```bash setup.sh``` from the command line to install requirements and create the virtual environment
* Run ```source ./assignment1_env/bin/activate```
* To run the script, run ```python3 src/code.py```
* If you want to see the results of a different target image than the default then run ```python3 src/code.py image_1300.jpg```. Here i just exemplify with image 1300, but you can chose any picture between 0001 and 1360.
* After running the script the results are located in the _out_ folder as "top_five.csv"
