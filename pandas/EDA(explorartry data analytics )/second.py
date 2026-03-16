import pandas as pd

df = pd.read_csv(r"C:\Users\saini\Downloads\countries of the world.csv")


print(df.shape)   # shape is used for the finding the rows and column.

print(df.head())   # head is used for the finding the first five rows and if there is noargument is given the its default value is 5.

print(df.tail())  #tailis for last five rows and if there is  no  argument is given then its default value is 5.

