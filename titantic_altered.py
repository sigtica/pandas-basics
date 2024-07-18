import pandas as pd
import numpy as np

dataset_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(dataset_url)
df

print(df.dtypes)

for column in df.columns:
    print(f"Value counts for the '{column}' column:")
    print(df[column].value_counts())
    print()

# Check the data type and number of unique values for each column
for column in df.columns:
    num_unique_values = df[column].nunique()
    data_type = df[column].dtype

    if num_unique_values <= 10:
        print(f"The '{column}' column is likely categorical, as it has {num_unique_values} unique values and a data type of {data_type}.")
    else:
        print(f"The '{column}' column is likely not categorical, as it has {num_unique_values} unique values and a data type of {data_type}.")

# Convert the categorical columns to one-hot encoded columns
df2 = pd.get_dummies(df, columns=['Survived','Pclass','Sex','SibSp','Parch','Embarked'], dtype=int)
df2

df2.dtypes

df2.to_csv('titanic_altered.csv', index=False)