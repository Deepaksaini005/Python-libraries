#Methods are the function that belongs to the object .

#creating class

class Student:
    def __init__(self , fullname):
        self.fullname = fullname
        
    def hello(self):
        print("Hello",self.fullname)
        
        #creting object 
    
s1 = Student("John")
s1.hello()
