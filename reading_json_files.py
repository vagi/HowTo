# Reading JSON files

import json

# open json file
with open('./files/sample_json.json','r') as file:
    data = json.load(file)

# json dictionary
print(type(data))

# loading into a DataFrame
df_json = pd.DataFrame(data)
df_json.head()


# But you can even load the JSON file directly into a dataframe using the pandas.read_json() function as shown below:

# reading directly into a DataFrame usind pd.read_json()
path = './files/sample_json.json'
df = pd.read_json(path)
df.head()
