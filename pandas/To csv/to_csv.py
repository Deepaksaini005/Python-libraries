import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
df.to_csv("outputdf.csv") 
df  = pd.read_csv("outputdf.csv")
print(df)


df.to_csv("outputdf_no_index.csv", index=False , header = ["A" , "B" , "C"])
df = pd.read_csv("outputdf_no_index.csv")
print(df)