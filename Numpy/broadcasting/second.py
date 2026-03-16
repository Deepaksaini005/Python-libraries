import  numpy  as  np

a1= np.arange(6).reshape(2,3)

print(a1*7)  #  multiply  by 7 


#broadcat (3,1) and (3,3) 

a2 = np.arange(3).reshape(3,1)
a3 = np.arange(9).reshape(3,3)

print(a2+a3)  

print(">>>>>>>>>")

print(a2*a3)