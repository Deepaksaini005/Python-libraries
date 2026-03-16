#drop na method - meanns if we have  missing value in our data frame we can remove that row or column using dropna method.
import pandas as pd
data = {
    "A": [1, 2, None, 4],
    "B": [5, None, 7, 8],
    "C": [9, 10, 11, None]
}
df = pd.DataFrame(data)
df_dropna = df.dropna()  # by default it removes row which has missing value
print(df_dropna)

df_dropna = df["A"].notna()  #  notna method return boolean values True/False
print(df_dropna)