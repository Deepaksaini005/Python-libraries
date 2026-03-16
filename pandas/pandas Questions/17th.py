# Create a new column "Age" using .iloc assignment, where Age = 2025 - Birth Year.

import pandas as pd

data = {
    "Name": ["Harry", "Mini", "Sofia", "Peter"],
    "City": ["Dispur", "Delhi", "Jaipur", "Mumbai"],
    "Role": ["Father", "Mother", "Sister", "Grand Father"],
    "Birth Year": [1968, 1978, 2002, 1947]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
df["Age"] = 2025 - df["Birth Year"]  # Create a new column "Age" using .iloc assignment, where Age = 2025 - Birth Year.
print(df)