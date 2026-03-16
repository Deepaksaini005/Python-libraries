# Modify the "Role" of all people in even-indexed rows to "Parent".

import pandas as pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

df.iloc[::2, 2] = "Parent"  # Modify the "Role" of all people in even-indexed rows to "Parent".
print(df)

