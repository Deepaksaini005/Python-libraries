import pandas as pd

df  = pd.read_csv(r"C:\Users\saini\Downloads\countries of the world.csv")

print(df.iloc[[2,4,5,6,3] ,[0,3,5,1]])  #show the specific rows and specific columns of the dataframe.


print(df.loc[[2,4,5,6,3] , ["Country","Population","Area (sq. mi.)","Region"]])  #show the specific rows and specific columns of the dataframe.
