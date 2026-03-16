#we can store a dictionary inside the dictionary is called the nested dictionary.
#Its a way to store multiple levels of the data

student={
    "name":"Abhii",
    "score": { 
       "chem":89,
       "math":90,
       "phy":85
        
    }
    
}

print(student)
print(student["score"]["math"])