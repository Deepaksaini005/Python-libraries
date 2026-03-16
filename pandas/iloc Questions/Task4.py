#  Task 4 — Logical Thinking

# - Use iloc to extract all rows except the first one.

# - Use negative indexing to show only the last column for all rows.


import pandas as pd
data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}

df = pd.DataFrame(data, index=["A", "B", "C", "D"])

print(df.iloc[1:4,0:4])  # Use iloc to extract all rows except the first one.


print(df.iloc[:,-1]) # Use negative indexing to show only the last column for all rows.