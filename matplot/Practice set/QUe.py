import numpy as np
import matplotlib.pyplot as plt 

sales =  np.random.randint( 1000 , 5000 , size = 12 ) 

ages =  np.array([18, 19, 20, 21, 22, 22, 23, 24, 25, 25 , 
        26, 27, 28, 28, 29, 30, 30, 31, 32, 33 , 
        34, 35, 36, 37, 38, 40, 42, 45, 48, 50])


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.plot(sales , marker = "o" , color = "green" )
cummsum_sales = np.cumsum(sales)
# cumsum is used to get cumulative sum of array elements
plt.plot(cummsum_sales , marker = "*" , color = "red" )
plt.title("Monthly Sales and Cumulative Sales")
plt.show()


# bar graph on horizontal axis

plt.barh(months, sales, color="purple", label="Monthly Sales" )
plt.barh(months, cummsum_sales, color="orange", label="Cumulative Sales" )

plt.show()

