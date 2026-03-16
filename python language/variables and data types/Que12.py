#WAP to  find the fctorial of a first n numbers (using for)

n=5
fact=1
for i in range(1,n+1):
  fact=fact*i  #fact*=i
  print("Factorial =" ,fact )
