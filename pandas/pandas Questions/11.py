# Use .iloc to display only rows 1 and 3, and columns 1 and 3.

import pandas as pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])


print(df.iloc[ 1:4 ,1:4])  # Use .iloc to display only rows 1 and 3, and columns 1 and 3.