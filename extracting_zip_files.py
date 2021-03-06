# Extracting from Zip Files

# import zipfile
from zipfile import ZipFile

# path to the zipfile
file = './files.zip'

# read zipfile and extract contents
with ZipFile (file, 'r') as zip:
    zip.printdir()
    zip.extractall()
    
