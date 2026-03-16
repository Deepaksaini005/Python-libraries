import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
temperatures = [22, 24, 19, 23, 25, 21, 20]


plt.axis([0, 8, 15, 30])  # in these first  2 values are for x-axis and last 2 values are for y-axis
plt.plot(days , temperatures , color ="r"  , marker = "o" , linestyle = "--")
plt.show()



from matplotlib import style

days = [1, 2, 3, 4, 5, 6, 7]
temperatures = [22, 24, 19, 23, 25, 21, 20]

style.use('ggplot')
plt.axis([0, 8, 15, 30])  # in these first  2 values are for x-axis and last 2 values are for y-axis
plt.plot(days , temperatures , color ="r"  , marker = "o" , linestyle = "--")
plt.show()