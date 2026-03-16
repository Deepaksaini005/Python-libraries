import pandas as pd

#channging the column names of the dataframe

student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

 

df = pd.DataFrame(student_data, columns=["A","B","C"])
print(df)


dataset1 = pd.read_csv(r"C:\Users\saini\Downloads\movies.csv")

print(dataset1.shape)   #shape method  tell the count of rows and columns in the dataframe

print(dataset1.head(2))  #head method returns the first n rows of the dataframe , by default it returns first 5 rows

print(dataset1.tail(2))  # tail method returns the last n rows of the dataframe , by default it returns last 5 rows

print(dataset1.columns)


print(dataset1.info())  #info method provides a concise summary of the dataframe including the number of non-null entries and data types of each column


print(dataset1.describe()) #describe method gives the statistical summary of numerical columns in the dataframe

print(dataset1.dtypes)  # it shows the data types of each column in the dataframe

print(dataset1.sample(5))  # it will return random 5 rows from the dataframe


print(dataset1.isnull().sum())  # it will return the count of null values in each column of the dataframe


print(dataset1.drop("tagline" , axis=1 , inplace=True))  # it will drop the specified column from the dataframe and  inplace=True will make the changes in the original dataframe.


print(df.sum(axis=1))  # it will return the sum of each row in the dataframe 


print(df.sum(axis=0))  # it will return the sum of each column in the dataframe

print(df.mean(axis =0))  # it will return the mean of each column in the dataframe 

print(df.mean(axis =1))  # it will return the mean of each row in the dataframe 


print(dataset1["title_x"])   # it will return the specified column from the dataframe

print(dataset1[["title_x", "year_of_release" , "actors"]])  # it will return multiple specified columns from the dataframe


print(dataset1.iloc[: , 4])  # it will return the specified column by index position from the dataframe


print(dataset1.loc[: ,"title_x"])  # it will return the specified column by label from the dataframe

print(dataset1.iloc[[1,8,14]])  # it will return the specified rows by index position from the dataframe