# Task 5 — Challenge Section

# - Print only “City” and “Birth Year” of the middle two records.

# - Modify the last two “Birth Year” values by adding +5.

# - Use a slice to display “Name” and “Role” for first three rows.

# - Get every second row (0, 2, …) using slicing.

import pandas as pd

Data = {
     "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}

df = pd.DataFrame(Data, index=["A", "B", "C", "D"])

print(df.iloc[: , 1:4:2])  # Print only “City” and “Birth Year” of the middle two records.

print(df.iloc[-2: , 3] + 5)  # Modify the last two “Birth Year” values by adding +5.


print(df.iloc[0:3 , 0:3:2]) # Use a slice to display “Name” and “Role” for first three rows.

print(df.iloc[::2])  # Get every second row (0, 2, …) using slicing.
