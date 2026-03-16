# Task 1 — Row & Column Access

# - Print the data for index “C”.
# - Print only the Name column for all rows.


import pandas as pd
data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}

df = pd.DataFrame(data, index=["A", "B", "C", "D"])

print(df.loc[["C"]])  # Print the data for index “C”.

print(df.loc[: , ["Name"]])  # print the name only column  .

