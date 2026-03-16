import pandas as pd

df  = pd.read_csv(r"C:\Users\saini\Downloads\countries of the world.csv")  
# print(df.iloc[201])  # Accessing the first row of the DataFrame using iloc

print(df.loc[201])


# Access the country at row index=2 and column name="Country"
print(df.loc[2, "Country"])  


#access the country at row index=2 and column index=0
print(df.iloc[2, 0])


#acess  the even data of the  dataframe
print(df.iloc[2: : 2])


#access  the first rows even and columns  5.
print(df.iloc[2::2 , 5])