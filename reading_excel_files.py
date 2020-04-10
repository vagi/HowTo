# Reading Excel files

# read Excel file into a DataFrame
df = pd.read_excel(r'./files/datas.xlsx')

# print first 5 rows of dataset
df.head()


# But an Excel file can contain multiple sheets. So how can we access them?
# For this, we can use the Pandas’ ExcelFile() function to print the names of all the sheets in the file:

# read Excel sheets in pandas
xl = pd.ExcelFile(r'./files/datas.xlsx')

# print sheet name
xl.sheet_names

# After doing that, we can easily read data from any sheet we wish by providing its name in 
# the sheet_name parameter in the read_excel() function:

# read Special sheet
df = pd.read_excel(r'./files/datas.xlsx',sheet_name='Special')
df.head()


