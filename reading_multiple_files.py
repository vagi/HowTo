# When importing multiple .py files from the same directory as your Python script, we can use the “*” wildcard:

for i in glob.glob('.\Importing files\*.py'):
    print(i)
    

# When importing only a 5 character long Python file, we can use the “?” wildcard:

for i in glob.glob('.\Importing files\?????.py'):
    print(i)
    

# When importing an image file containing a number in the filename, we can use the “[0-9]” wildcard:

for i in glob.glob('./Importing files/test_image[0-9].png'):
    print(i)
    

# Earlier, we imported a few images from the Wikipedia page on Odesa and saved them in a local folder. 
# I will retrieve these images using the glob module and then display them using the PIL library:

import cv2
import matplotlib.pyplot as plt

# import glob

filepath = r'./Importing files/Odesa'

images = glob.glob(filepath+'\*.jpg')

for i in images[:3]:
    im = Image.open(i)
    plt.imshow(im)
    plt.show()
