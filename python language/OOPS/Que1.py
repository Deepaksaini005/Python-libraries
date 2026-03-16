#Create student  class that takes name & marks of 3 subjects  as argumnents in constructor .Then create a method to print the average .

#create the class 

# Create student class
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
    # Method to print the average of marks
    
    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

# Create an object and call the metho

s1 = Student("Rahul", 90, 80, 70)

print(s1.average())
