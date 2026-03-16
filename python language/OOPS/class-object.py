class Student:
    college_name="ABC College"

    def __init__(self,name,marks):
        self.name =  name 
        self.marks = marks
        print("adding a student in a database")
        
        
s1 = Student("ram",89)
print(s1.name ,s1.marks)      #ram

s2 = Student("shyam",99)
print(s2.name,s2.marks)      #shyam

print(s2.college_name)