#Extract subsets of data using each method .

import pandas as pd

data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
}

df = pd.DataFrame(data)
#subset of data
subset = df.loc[:1, ["A", "C"]]
print(subset)


#______________#
subset["slice_loc"] =subset.loc[:1,"C"] = df.loc[:1, "C"]  #slicing using loc
print(subset)



#______________#
subset.insert(2, "A_copy", df["A"] )  #cloning using insert method
print(subset)
