#  Task 2 — Slicing

#  - Display rows 0 to 2 and columns 1 to 3.

# - Display last two rows and last two columns.

import pandas as  pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}

df =pd.DataFrame(data , index =["A", "B", "C", "D"])

print(df.iloc[0:3,1:4])  # Display rows 0 to 2 and columns 1 to 3. - positive indexing

print(df.iloc[-2:,-2:])  # Display last two rows and last two columns.  - negative indexing 
