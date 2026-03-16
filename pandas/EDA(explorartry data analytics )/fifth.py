import pandas as pd

df  = pd.read_csv(r"C:\Users\saini\Downloads\countries of the world.csv")
print(df.loc[0:228 , "Country"])  

print(df.loc[200]) # Accessing the  row of the DataFrame using loc that shows the complete information of that row.


print(df.loc[0:228:5])  #acces the rows from 0 to 228 with the step size of 5.





