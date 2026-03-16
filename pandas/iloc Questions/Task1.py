#  Task 1 — Row & Column Basics

#    - Print the 2nd row.
#    - Print first and third rows.
#    - Print “Role” column using column position.


import  pandas as  pd 

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}

df =pd.DataFrame(data , index =["A", "B", "C", "D"])
print(df.iloc[1])  # Print the 1st row.

print(df.iloc[0 :2]) # Print first and third rows.

print(df.iloc[:,2]) # Print “Role” column using column position.