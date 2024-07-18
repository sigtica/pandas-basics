# Question 1: when importing dependencies, what is the norm for pandas and numpy?
# import pandas as .........
import pandas        # <---- as what? .......
import numpy         # <---- as what? .......

# Question 2: use pandas to read a CSV file into the runtime and call the object 'df'
dataset_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = # ...

# Question 3: create new column in the same dataframe called "age_in_months", which multiplies "Age" by 12

# Question 3b: bonus question: try changing the dtype of "age_in_months" to "int64". Can you do it? Why or why not?

# Question 4: are there missing values (NaN) in "Age"?
# Slice the dataframe to only show rows here Age is NaN (but do not overwrite the original dataframe)

# Question 5: now slice the titanic dataframe so that you only see rows where Pclass==1, and save it as a new
# dataframe called df2

# Question 6: for df2, only keep columns: Age, Name, Sex, Fare, Survived, PassengerId (in this order), overwriting df2

# Question 7: create a new column in df2 called "age_dummy", which is equal to 1 if age>27, and 0 if age<=27

# Question 8. create a new column called "group1" which is equal to 1 if (Sex is "female") AND (age is greater than 33), and 0 otherwise

# Question 9. What is the age of a passenger named "Carrau, Mr. Francisco M"?
# Give me the actual number inside the cell, using pandas (not pd.Series or pd.DataFrame)

# Question 10. what is the difference (type) between df2[['Name']] and df2['Name']?

# Question 11. how to change the value of a specific cell(s)?
# I want to change the value of "Age" for all that Survived and are Female to 18 (18 years old)

# Question 12. For all missing values for "Fare", fill them with -99.

# Question 13. write a lambda function that takes "Fare", and runs it through this function: 1000*((Fare*2)/1.5)**8 (to the power of 8).
# call this 'Fare_adjusted' as a new column in the dataframe

# Question 14. Break up the "Name" column into two columns: df['last_name'] and df['given_name'] (split by comma ",")
# e.g. "McCarthy, Mr. Timothy J" ==> "McCarthy" and "Mr. Timothy J"

# Question 15. sort this dataframe in ascending order for "Age"

# Question 16. Reset the index of this dataframe

# Question 17. chop this dataframe into 3 chunks:
# chunk 1: 0 to 100th row
# chunk 2: 101st to 200th row
# chunk 3: everything else beyond the 200th row
# call them chunk1, chunk2, chunk3

# Question 18. then concat these 3 dataframes vertically so that the final product
# is the SAME as the original df2 dataframe, and call this
# concat dataframe "df3"

# Question 19. Group the dataframe df3 by 'Sex' and call it "df3_grouped", then get a list of the keys

# Question 20. Get the 'male' dataframe slice from "df3_grouped"

# Question 21. create two separate dataframes from df2
# t1 = dataframe 1: only includes Fare and Name
# t2 = dataframe 2: only includes Name and Sex
# use concat axis=1 to horizontally concat them so that you have a final dataframe of 4 columns: Fare, Name, Name, Sex
# please check to make sure the rows are also 216, like the original dataset

# Question 22. This time use the "merge" feature to merge t1 with t2 using on=["Name"]. How come there are only 3 columns?

# Question 23. create a new dataframe t3 which only keeps the first 100 rows, then merge with t2 again. what do you see?
# t3.merge(t2, on=["Name"])

# Question 24. how to transpose matrix so that the columns become rows and the rows become columns? (using df2)

# Question 25. how to get a list of column names of df2?





