# Reading CSV file

# import pandas
import pandas as pd

# read csv file into a DataFrame
df = pd.read_csv(r'./files/data.csv')

# display DataFrame
df.head()
df.tail()


"""
But CSV can run into problems if the values contain commas. 
This can be overcome by using different delimiters to separate information in the file, 
like ‘\t’ or ‘;’, etc. These can also be imported with the read_csv() function by specifying 
the delimiter in the parameter value as shown below while reading a TSV (Tab Separated Values) file:
""" 

df = pd.read_csv(r'./files/file.txt',delimiter='\t')
df.head()


"""
Reading CSV file in Russian language - encoding cp1251
"""
df = pd.read_csv("file.csv", encoding='cp1251', delimiter=';')

