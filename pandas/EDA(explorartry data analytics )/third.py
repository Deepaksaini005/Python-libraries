import pandas as pd


df  = pd.read_csv(r"C:\Users\saini\Downloads\countries of the world.csv")


pd.set_option("display.max_columns",22) # this method is used for the displaying the all columns of the dataframe.
print(df)  

pd.set_option("display.max_rows", 230)  # this method is used for the displaying the all rows of the dataframe.
print(df)