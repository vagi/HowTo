# Reading Text Files

"""
Python provides the open() function to read files that take in the file path and the file access mode as its parameters. For reading a text file, the file access mode is ‘r’. I have mentioned the other access modes below:

‘w’ – writing to a file
‘r+’ or ‘w+’ – read and write to a file
‘a’ – appending to an already existing file
‘a+’ – append to a file after reading
"""

# read text file
with open(r'./Importing files/Analytics Vidhya.txt','r') as f:
    print(f.read())

