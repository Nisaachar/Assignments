import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('arrhythmia.data')
attributes = data.select_dtypes(include=['float64', 'int64'])
scaler = StandardScaler()
data = scaler.fit_transform(attributes)
dataframe = pd.DataFrame(data, columns=attributes.columns)
print(dataframe.head(10))
