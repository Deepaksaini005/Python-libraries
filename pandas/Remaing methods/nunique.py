import pandas as pd

df = pd.DataFrame({
    'fruit': ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'],
    'color': ['red', 'yellow', 'green', 'orange', 'yellow', 'red']
})

print(df["fruit"].nunique()) #count of the unique values  


print(df["color"].unique())  # unique tells the list of the unique values