import pandas as pd

#second csv dat  set operations.

dataset2 = pd.read_csv(r"C:\Users\saini\Downloads\ipl-matches.csv")

# print(dataset2.shape)  
# print(dataset2)
# print(dataset2.columns)

# print(dataset2)
# print(dataset2.to_string())


mask = dataset2["MatchNumber"]=="Final"
print(dataset2[mask])  # it will return all the rows where the condition is true

print(dataset2[dataset2["MatchNumber"]=="Final"][["Season" , "WinningTeam"]])