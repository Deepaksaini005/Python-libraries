import pandas as pd 

df1 = pd.DataFrame({"A":[2,3,4]  , "B":[4,6,2]})
df2 = pd.DataFrame({"A": [9,4,6] , "B":[4,7,5]})
df3 = pd.concat([df1 , df2] , axis = 1)
print(df3)