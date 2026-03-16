"""You are given this condition:
People born before 1970 are “Senior”, others are “Junior”.
Add a new column "Category" using .iloc to store this classification."""

import pandas as pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

df["Category"] = df.apply(
    lambda row: "Senior" if row["Birth Year"] < 1970 else "Junior" , axis=1)

print(df)