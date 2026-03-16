# Replace the Role in row 1 with "Manager" using .iloc.


import pandas as pd


data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])


df.iloc[ 1 ,2 ] = "Manager"  # Replace the Role in row 1 with "Manager" using .iloc. 
print(df)