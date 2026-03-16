import pandas as pd

data =  ["Alice", "Bob", "Charlie"]
val = [25, 30, 35]

df =pd.DataFrame([data  , val] , index = ["name" , "age"] )
print(df)


df = pd.DataFrame({"name": data, "age": val})
print(df)