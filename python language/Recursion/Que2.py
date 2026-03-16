"""write a recursive  function to print all the elements in a list 
Hint : use lis & index as parameters """



fruits = ["mangoes", "apple","orange","banana","litchi","kivi","nuts"]   #this  is the list of the fruits 


def print_list(list, idx = 0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)
print_list(fruits)
    