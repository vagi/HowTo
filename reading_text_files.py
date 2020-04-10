# Reading Text Files

"""
Python provides the open() function to read files that take in the file path and the file access mode as its parameters. For reading a text file, the file access mode is ‘r’. I have mentioned the other access modes below:

‘w’ – writing to a file
‘r+’ or ‘w+’ – read and write to a file
‘a’ – appending to an already existing file
‘a+’ – append to a file after reading

Python provides us with three functions to read data from a text file:

read(n) – This function reads n bytes from the text files or reads the complete information from the file if no number is specified. It is smart enough to handle the delimiters when it encounters one and separates the sentences
readline(n) – This function allows you to read n bytes from the file but not more than one line of information
readlines() – This function reads the complete information in the file but unlike read(), it doesn’t bother about the delimiting character and prints them as well in a list format
"""

# read text file
with open(r'./Importing files/Analytics Vidhya.txt','r') as f:
    print(f.read())
    
    
# read text file
with open(r'./Importing files/Analytics Vidhya.txt','r') as f:
    print(f.read(10))
    
 
# read text file
with open(r'./Importing files/Analytics Vidhya.txt','r') as f:
    print(f.readline())
    
    
# read text file
with open(r'./Importing files/Analytics Vidhya.txt','r') as f:
    print(f.readlines())
    
