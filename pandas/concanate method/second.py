
import pandas as pd 
# January Sales Data
jan = pd.DataFrame({
    'Order_ID': [101, 102, 103],
    'Product': ['Shoes', 'Bag', 'Watch'],
    'Sales': [120, 80, 150],
    'Month': ['January'] * 3
})

# February Sales Data
feb = pd.DataFrame({
    'Order_ID': [104, 105, 106],
    'Product': ['Shoes', 'Belt', 'Watch'],
    'Sales': [200, 50, 130],
    'Month': ['February'] * 3
})

# March Sales Data
mar = pd.DataFrame({
    'Order_ID': [107, 108, 109],
    'Product': ['Shoes', 'Bag', 'Perfume'],
    'Sales': [180, 95, 110],
       'Month': ['March'] * 3
})
    
jan.to_csv('sales_january.csv', index=False)
feb.to_csv('sales_february.csv', index=False)
mar.to_csv('sales_march.csv', index=False)

# in teno jo ek sath lane ke liye concat ka  use  kra h 

sales_concanate = pd.concat([jan ,  feb, mar] , ignore_index=True)
print(sales_concanate)