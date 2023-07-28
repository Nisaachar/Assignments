import pandas as pd

data = pd.read_csv('arrhythmia.data')
bin_suffix = ['Bin' + str(i) for i in range(1, 11)]
for column in data.columns:
    if data[column].dtype != 'object':
        data[column] = pd.cut(data[column], bins=10, labels=bin_suffix)
records = data.head(10)
print(records)
