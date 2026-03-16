#del keyword is used to delete the object properties or object itself.

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
s1 =  student("John",30)
print(s1.name)    #this can print the name  after that
del s1.name  #use del keyword to delete the object property
print(s1.name)   #in the he can del the name  annd shows an error
            
      