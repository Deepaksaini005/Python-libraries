
#there is the two parent class .

class Father:
    
    def skills (self):
        print("Father: Cooking,Driving")
        
class Mother:
    def skills (self):
        print("Mother: Singing,Painting")
        
#child inheritate properties from his parents 

class Child(Father ,Mother):
    def skills (self):
        print("Child skills : Playing, Coding ")
        Father.skills(self)
        Mother.skills(self)

        
# create object for the child 

c = Child()
c.skills()
        