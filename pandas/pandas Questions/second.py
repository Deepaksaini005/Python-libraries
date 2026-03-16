# Show the first three rows but only the City and Role columns.


import pandas as pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])


print(df.iloc[0:3 , 1:3])  # Show the first three rows but only the City and Role columns.