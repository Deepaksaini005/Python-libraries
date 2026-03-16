import pandas as pd

df = pd.DataFrame({
    'fruit': ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'],
    'color': ['red', 'yellow', 'green', 'orange', 'yellow', 'red']
})

# print(df["fruit"].drop_duplicates())
# print(df["color"].drop_duplicates())
# print(df.duplicated(subset=["color"]))  #subset use here for the shows that  it present in these  data .
print(df.groupby('fruit').size())