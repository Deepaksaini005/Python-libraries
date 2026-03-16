import  numpy as np 

#ittrating the values of the 1D array and 2D array
arr_1D = np.array([1,2,3])
arr_2D =np.array([[3,4,5],[6,7,8] ])

for item in arr_1D:
    print(item)
for i in arr_2D:
    for j in i:
        print(j)
