#  Task 2 — Conditional Selection

# - Find all people born before 1980.

# - Find the City of all people whose Role contains the word "Father".  

import pandas as pd

Data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}

df = pd.DataFrame(Data, index=["A", "B", "C", "D"])

#show the data if ["Birth Year"]]<1980) these happens . 

print(df.loc[:,["Birth Year"]]<1980)  


#for father in role then the cites show for it .
mask = df['Role'].apply(lambda role: 'Father' in role)

father_cities = df.loc[mask, 'City']
print(father_cities)





