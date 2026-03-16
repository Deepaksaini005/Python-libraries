#WAP to  return n! in thhe output.

def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n

print(fact(3))

#  Another  method for these question ---



# num  = int(input("Enter a Number:"))

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return fact(n-1)*n
# print("factorial is :" ,fact(num))