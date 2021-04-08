# All data to be mapped to float or integers (in case we will normalize whole dataset)
# and drop the unrequired columns.

# First map the string values of target to integer (we have categorical values here) .

def mapping(data, feature):
    featureMap = dict()
    count=0
    for i in sorted(data[feature].unique(),reverse=True):
        featureMap[i] = count
        count = count+1
    data[feature] = data[feature].map(featureMap)
    return data

data = mapping(data, "diagnosis")


# Normalizing a single row.
data["concavity_mean"] = ((data["concavity_mean"]-data["concavity_mean"].min())/(data["concavity_mean"].max()-data["concavity_mean"].min()))*20


# Normalizing entire dataframe.
dataf = ((data-data.min())/(data.max()-data.min()))*20


# Normalizing entire dataframe excluding a one or few columns.
def normalize(dataset):
    dataNorm = ((dataset-dataset.min())/(dataset.max()-dataset.min()))*20
    dataNorm["diagnosis"] = dataset["diagnosis"]
    return dataNorm

data=normalize(data)


# So this was all about normalizing a dataframe. 
# This tutorial was made because standard scalars work only on numpy arrays and if we 
# try to convert dataframes to numpy array, we'll lose column names. Hope you like it.
