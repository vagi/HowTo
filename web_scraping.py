import requests

# url = "https://weather.com/en-IN/weather/today/l/UPXX0021:1:UP"
url = "https://en.wikipedia.org/wiki/Odesa"

# response object
resp = requests.get(url)

# using text attribute of the response object, return the HTML of webpage as string
text = resp.text

print(text)


# Calling prettify() on BeautifulSoup object parses the tree-like structure of the HTML document:

import requests
from bs4 import BeautifulSoup

# url
# url = "https://weather.com/en-IN/weather/today/l/UPXX0021:1:UP"
url = "https://en.wikipedia.org/wiki/Odesa"

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the response
print(soup.prettify())


# Now, we can extract the title of the webpage by calling the title() function of our soup object:

title = soup.title
title


"""
The webpage has a lot of pictures of the famous monuments in Delhi and other things related to Delhi. 
Let’s try and store these in a local folder.
We will need the Python urllib library to retrieve the URL of the images that we want to store. 
It has a urllib.request() function that is used for opening and reading URLs. Calling the urlretrieve() 
function on this object allows us to download objects denoted by the URL to a local file:

import urllib

# function to save image from the passed URL
def download_img(url, i):
    
#  folder = r'C:\Users\...\'
    folder = r'./Importing files/Odesa/'
    
    # define the file path to store images
    filepath = folder + str(i) +'.jpg'
    
    # retrieve the image from the URL and save in the folder
    urllib.request.urlretrieve(url,filepath)


"""
The images are stored in the “img” tag in HTML. These can be found by calling find_all() 
on the soup object. After this, we can iterate over the image and get its source by calling 
the get() function on the image object. The rest is handled by our download function:

images = soup.find_all('img')
i = 1
for image in images[2:10]:
    try:
        download_img('https:'+image.get('src'), i)
        i = i+1
    except: 
        continue
        




