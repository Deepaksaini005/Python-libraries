#search for a number x in tthis tuple using loop.
#  [1,4,9,16,25,36,49,64,81,100,49]

tup= (1,4,9,16,25,36,49,64,81,100,49)
x=49
i=0 #  here i is index variable
for num in tup:
    if (num==x):
        print("x is found at i",i)
        break
    i+=1
    