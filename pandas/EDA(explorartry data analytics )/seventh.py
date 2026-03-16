import pandas as pd
df  = pd.read_csv(r"C:\Users\saini\Downloads\countries of the world.csv")

print(df.rename(columns={"Country":"contry" }))

# this method is used for the renaming the columns of the dataframe.

print(df.drop(columns ="Country") ) # this method is used for the dropping  or removing the columns of the dataframe.3