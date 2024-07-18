# Question 1: when importing dependencies, what is the norm for pandas and numpy? import pandas as .........
import pandas as pd        # <---- as what? .......
import numpy as np         # <---- as what? .......

# Question 2: use pandas to read a CSV file into the runtime and call the object 'df'
dataset_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(dataset_url)
df

# Question 3: create new column in the same dataframe called "age_in_months", which multiplies "Age" by 12
df['age_in_months'] = df['Age']*12
df

# Question 3b: bonus question: try changing the dtype of "age_in_months" to "int64". Can you do it? Why or why not?
df['age_in_months'].astype('int64')

# because int64 requires every single cell to have something in it; if there is a NaN, it will not work.
# however, if you use the .fillna(-99) command, you can after that.
df['age_in_months'].fillna(-99).astype('int64')

# Question 4: are there missing values (NaN) in "Age"?
# Slice the dataframe to only show rows here Age is NaN (but do not overwrite the original dataframe)
df[df['Age'].isnull()==True]

# Question 5: now slice the titanic dataframe so that you only see rows where Pclass==1, and save it as a new
# dataframe called df2
df2 = df[df['Pclass']==1]
df2

# Question 6: for df2, only keep columns: Age, Name, Sex, Fare, Survived, PassengerId (in this order), overwriting df2
df2 = df2[['Age','Name','Sex','Fare','Survived','PassengerId']]
df2

# Question 7: create a new column in df2 called "age_dummy", which is equal to 1 if age>27, and 0 if age<=27

# there are two ways. using np.where():
df2['age_dummy_method1'] = np.where(df2['Age']>27, 1, 0)
df2

# using .loc[row_indexer,col_indexer] = value
df2.loc[df2['Age']>27, 'age_dummy_method2'] = 1 # <--- this will create 1 only for age>27, but leaves age<=27 as NaN
df2['age_dummy_method2'] = df2['age_dummy_method2'].fillna(0)  # <--- this fills in 0 for age<=27
df2['age_dummy_method2'] = df2['age_dummy_method2'].astype('int64') # <--- ensures that the dummy is int64, not float64
df2

# Question 8. create a new column called "group1" which is equal to 1 if (Sex is "female") AND (age is greater than 33), and 0 otherwise
df2['group1'] = np.where((df2['Age']>33)&(df2['Sex']=='female'), 1, 0)
df2

# Question 9. What is the age of a passenger named "Carrau, Mr. Francisco M"?
# Give me the actual number inside the cell, using pandas (not pd.Series or pd.DataFrame)
df2[df2['Name']=="Carrau, Mr. Francisco M"]['Age'].tolist()[0]

# Question 10. what is the difference (type) between df2[['Name']] and df2['Name']?
df2[['Name']] # <--- pd.DataFrame

df2['Name'] # <--- pd.Series

# Question 11. how to change the value of a specific cell(s)?
# I want to change the value of "Age" for all that Survived and are Female to 18 (18 years old)
df2.loc[(df2['Survived']==1)&(df2['Sex']=='female'),'Age'] = 18
df2

# Question 12. For all missing values for "Fare", fill them with -99.
df2['Fare'] = df2['Fare'].fillna(-99)
df2

# Question 13. write a lambda function that takes "Fare", and runs it through this function: 1000*((Fare*2)/1.5)**8 (to the power of 8).
# call this 'Fare_adjusted' as a new column in the dataframe
df2['Fare_adjusted'] = df2['Fare'].apply(lambda x: 1000*((x*2)/1.5)**8)
df2

# Question 14. Break up the "Name" column into two columns: df['last_name'] and df['given_name'] (split by comma ",")
# e.g. "McCarthy, Mr. Timothy J" ==> "McCarthy" and "Mr. Timothy J"
df2['last_name'], df2['given_name'] = zip(*df2['Name'].apply(lambda x: x.split(',')))
df2

# Question 15. sort this dataframe in ascending order for "Age"
df2 = df2.sort_values(by=['Age'], ascending=True)
df2

# Question 16. Reset the index of this dataframe
df2 = df2.reset_index(drop=True)
df2

# Question 17. chop this dataframe into 3 chunks:
# chunk 1: 0 to 100th row
# chunk 2: 101st to 200th row
# chunk 3: everything else beyond the 200th row
# call them chunk1, chunk2, chunk3
chunk1 = df2[0:100]
chunk2 = df2[100:200]
chunk3 = df2[200:]
print('chunk1', len(chunk1))
print('chunk2',len(chunk2))
print('chunk3',len(chunk3))

# Question 18. then concat these 3 dataframes vertically so that the final product
# is the SAME as the original df2 dataframe, and call this
# concat dataframe "df3"
df3 = pd.concat([chunk1, chunk2, chunk3])
df3

# Question 19. Group the dataframe t3 by 'Sex' and call it "grouped", then get a list of the keys
grouped = df3.groupby('Sex')
list(grouped.groups.keys())

# Question 20. Get the 'male' dataframe from the grouped
grouped.get_group('male')

# Question 21. create two separate dataframes from df2
# t1 = dataframe 1: only includes Fare and Name
# t2 = dataframe 2: only includes Name and Sex
# use concat axis=1 to horizontally concat them so that you have a final dataframe of 4 columns: Fare, Name, Name, Sex
# please check to make sure the rows are also 216, like the original dataset
t1 = df2[['Fare','Name']]
t2 = df2[['Name', 'Sex']]
pd.concat([t1, t2], axis=1)

# Question 22. This time use the "merge" feature to merge t1 with t2 using on=["Name"]. How come there are only 3 columns?
t1.merge(t2, on=['Name'])

# Question 23. create a new dataframe t3 which only keeps the first 100 rows, then merge with t2 again. what do you see?
# t3.merge(t2, on=["Name"])
t3 = t1[0:100]
t3.merge(t2, on=["Name"])

# Question 24. how to transpose matrix so that the columns become rows and the rows become columns? (using df2)
df2.T

# Question 25. how to get a list of column names of df2?
df2.columns.tolist()





