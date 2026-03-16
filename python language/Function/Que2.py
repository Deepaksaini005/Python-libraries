#if there is no argument is nnot passed then the the defulaut parameter is used.

def calc_prod(a=3,b=4):   # here 3 & 4 work  as default parameters
    print(a*b)
    return a*b
calc_prod()   #there is no parameters 
    