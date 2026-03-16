#search for a number x in this tuple usinng loop.
# (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,49,64,81,100 ,36)

x= 4
i=0
while i<len(nums):
    if (nums[i]==x):
        print("found at index",i)
        break
    i+=1
print("found")
    
        
