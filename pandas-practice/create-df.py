import pandas as pd

# ------- creating a data frame -------
column = ['athoug', 'batman', 'iron man']
titled_columns = {
    "name": column,
    "height": [1.55, 1.9, 1.7],
    "weight": [64, 100, 90]
}
data = pd.DataFrame(titled_columns)
print(data)

# ------- selecting values in a dataframe -------
# viewing teh weight column
print(data['weight'])
# viewing the batman name
print(data['name'][1])

# we can also view entire row
athoug = data.iloc[0]
print(athoug)


# ------- Manipulating dataframes -------
# bmi = weight / height**2
bmi = []
for i in range(len(data)):
    bmi_score = data['weight'][i] / (data['height'][i]**2)
    bmi.append(bmi_score)

data['bmi'] = bmi
print(data)


# ------- save dataframe to file -------
data.to_csv('./bmi.csv', index=False)
data.to_csv('./bmi.txt', sep='\t')
