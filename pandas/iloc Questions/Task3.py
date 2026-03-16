# Task 3 — Updating Values

# - Change the first person’s name to “Henry”.

# # - Change the city of the last person to “Kolkata”.


import pandas as  pd
data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}

df =pd.DataFrame(data , index =["A", "B", "C", "D"])

df.iloc[0,0]  = "Henry"  # original value
print(df)  # Change the first person’s name to “Henry”.

df.iloc[-1 , 1] = "Kolkata"  # original value
print(df)  # Change the city of the last person to “Kolkata”.
