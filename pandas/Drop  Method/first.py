import  pandas as pd 

data = {
    "A": [10, 20, 30, 40],
    "B": [50, 60, 70, 80],
    "C": [90, 100, 110, 120],
    "D":[20,30 ,49, 40]
}

df = pd.DataFrame(data)
# Dropping column B
df_dropped = df.drop(columns=["B", "D"])  # these method we can remove multiple columns.

print(df_dropped)

