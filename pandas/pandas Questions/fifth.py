

# Change the city of the first person to "Kolkata".


import pandas as pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

df.iloc[0,1] = "Kolkata"  # Change the city of the first person to "Kolkata".
print(df)