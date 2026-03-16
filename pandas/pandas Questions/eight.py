# Display only the first and last columns for all rows.

import pandas as pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

print(df.iloc[0 :, [0, -1]])  # Display only the first and last columns for all rows.