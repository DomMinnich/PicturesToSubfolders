Description
The Picture Mover is a simple GUI application built using Python's Tkinter library. It provides a convenient way to organize pictures by moving them from a selected picture folder to multiple subfolders within another directory. This can be particularly useful for sorting and categorizing large collections of images.

Features
Select a directory containing subfolders.
Select a picture folder containing the images to be moved.
View the total number of subfolders and pictures.
Calculate the ratio of pictures to subfolders.
Move pictures evenly into each subfolder based on the selected ratio.

Requirements
Python 3.x
Tkinter (usually comes pre-installed with Python)
shutil (a standard library module for file operations)
datetime (a standard library module for date and time operations)

Installation
No installation is required. Simply download the provided code and run it using Python.

Usage
Run the script.
Click on "Choose Directory" to select a directory containing subfolders.
Click on "Choose Picture Folder" to select a folder containing pictures to be moved.
Review the displayed information about the total number of subfolders and pictures, and the calculated ratio.
Click on "Move Pictures" to start the moving process.
Upon completion, a success message will be displayed.

Note
Ensure that the ratio of pictures to subfolders is a whole number for the moving process to proceed smoothly.
Subfolders are created based on the current date in the format "MM_DD_YYYY" within each selected subfolder.

Author
This application was created by Dominic Minnich, April 2024
