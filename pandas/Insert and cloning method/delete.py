#delete  method
import pandas as pd
data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"], "Age": [55, 50, 20, 70] , "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"]
}

df = pd.DataFrame(data, index=["A", "B", "C", "D"])
df.pop("Age")   # this is the delete method .
print(df)

del df["City"]   # this is another delete method .
print(df)