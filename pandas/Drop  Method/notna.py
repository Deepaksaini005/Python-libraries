#notna mathod in pandas - it return boolean values True/False if value is not missing then it return True otherwise False.
import pandas as pd
data = {
    "A": [1, 2, None, 4],
    "B": [5, None, 7, 8],
    "C": [9, 10, 11, None]
}

df = pd.DataFrame(data)
df_notna = df["A"].notna()  #  notna method return boolean values True/False
print(df_notna)


df_valna=df.notna().sum()  # it count total not missing values in each column
print(df_valna)

df_mean = df.notna().mean()*100  # it calculate the mean of not missing values in each column in percentage
print(df_mean)
