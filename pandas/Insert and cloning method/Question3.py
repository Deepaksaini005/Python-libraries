#Modify the data using slice assignmennt 

import pandas as pd
data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
}
df = pd.DataFrame(data)
df.loc[:1, "C"] = [70, 80]  # Modifying the first two rows of column C using slice assignment
print(df)   



