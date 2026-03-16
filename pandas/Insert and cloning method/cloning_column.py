import pandas as pd  

data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6]
}
df = pd.DataFrame(data)

# Insert a new column "A++" that copies or modifies column "A"
df.insert(2, "A++", df["A"] )

print(df)