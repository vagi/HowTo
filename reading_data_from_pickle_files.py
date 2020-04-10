# Reading data from Pickle files

import pickle

with open('./files/sample_pickle.pkl','rb') as file:
    data = pickle.load(file)

# pickle data
print(type(data))

df_pkl = pd.DataFrame(data)
df_pkl
