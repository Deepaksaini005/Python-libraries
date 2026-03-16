import pandas as pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"], "Age": [55, 50, 20, 70] , "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

df.insert(2,"counrty" , ["India", "Canada", "India", "USA"])   #this is the insert method .

print(df)   