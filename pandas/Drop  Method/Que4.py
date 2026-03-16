
# Drop rows where Quantity == 0.
# Drop rows where Region = 'South'.
# Keep only rows where Price ≥ 200 and Quantity > 5.

import pandas as pd 

data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Price': [100, 200, 150, 300, 250],
    'Quantity': [5, 0, 10, 8, 0],
    'Region': ['North', 'South', 'East', 'West', 'South']
}
sales = pd.DataFrame(data)