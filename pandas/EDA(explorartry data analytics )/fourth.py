import pandas as pd
df  = pd.read_csv(r"C:\Users\saini\Downloads\countries of the world.csv")


df.info()   # info is used for find the info about the data frame like rows , columns , non-null count and dtypes.



print(df.describe())  #describe is used for the find the static analysis of the dataframe like count , mean , std , min , 25% , 50% , 75% and max.




