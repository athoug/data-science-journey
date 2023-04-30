import pandas as pd
import numpy as np
# ------- load data ----------
data = pd.read_csv('./data/pokemon_data.csv')
data_txt = pd.read_csv('./bmi.txt', sep='\t')

# view only first 3 records
print(data.head(3))

# view last 2 rows
print(data.tail(3))


# ------- filtering data -------
grass_pokemon = data[data['Type 1'] == 'Grass']
print(grass_pokemon)

# replace values
Nan_data = data.replace(np.nan, 'empty')
print(Nan_data)


# remove data
# note axis 1 is columns and axis 0 is rows
Nan_data.drop('Generation', axis=1, inplace=True)
Nan_data.drop(0, axis=0, inplace=True)
print(Nan_data)
