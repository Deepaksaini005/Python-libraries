
#these method for the drop duplicates
import pandas as pd
data = {
    "A": [1, 2, 2, 4], 
    "B": [5, 6, 6, 8],
    "C": [9, 10, 10, 12]
}
df = pd.DataFrame(data)


df_drop_duplicate = df.drop_duplicates()
print(df_drop_duplicate)