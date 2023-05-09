from os import listdir
from os.path import isfile, join, isdir
from PIL import Image
import matplotlib.pyplot as plt

def read_images_in_folder(path):
    """
    This function reads every image inside a folder and every folder inside that folder.

    Parameters:
    path (str): The path of the folder to be read.

    Returns:
    None
    """
    # Get a list of all files and directories in the given path
    files_and_directories = listdir(path)
    # Loop through all files and directories
    for file_or_dir in files_and_directories:
        # If the current item is a file, check if it is an image file and read it if it is
        if isfile(join(path, file_or_dir)):
            if file_or_dir.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                img = Image.open(join(path, file_or_dir))
                # Do something with the image here
                plt.imshow(img)
                plt.show()
                img.close()

        # If the current item is a directory, call this function recursively on that directory
        elif isdir(join(path, file_or_dir)):
            read_images_in_folder(join(path, file_or_dir))


def main():
    read_images_in_folder('/Users/ozlemyildiz/Desktop/Image/Project/MLMR-COS/')


main()