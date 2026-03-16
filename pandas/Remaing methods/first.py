import pandas as pd 


s = pd.Series(["Apple" , "Banana" ," Orange" , "Apple" , "Banana" ," Orange"])

print(s.value_counts())

df = pd.DataFrame({
    'fruit': ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'],
    'color': ['red', 'yellow', 'green', 'orange', 'yellow', 'red']
})

print(df["fruit"].value_counts())  #vlaue_count mmethod is used to cound value .