import numpy as np 


def sigmoid(array):  # sigmoid function
    return 1 / (1 + np.exp(-array))

a  = np.arange(100)
print(sigmoid(a))



# import matplotlib.pyplot as plt
# x = np.linspace(-10, 10, 100)
# y = 1 / (1 + np.exp(-x))
# plt.plot(x, y)
# plt.show()



actual = np.random.randint(1 ,50 ,25)
predicted = np.random.randint(1 ,50 ,25)

def mse(act, pred):
    return np.mean((actual - predicted) ** 2)
print(mse(actual, predicted))

