# Nesting means placing one if statement inside another if statemage . 

age = int(input("age:"))
if (age>=18):
    if(age>=70):
        print("Can't drive")
    else:
        print("can drive ")
else:
        print ("can't drive  ")  # This will never be printed because the first if condition