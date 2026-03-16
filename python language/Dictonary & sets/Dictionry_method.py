#there RE THE MANY METHODS OF  THE  DICTIONARY
#1. myDict.keys()   - return all keys
#2. myDict.values()    - return all values 
#3. myDict.items()   - return all (key-value) pairs as tuple
#4. myDict.get("key")   - return themkey according to the value
#5. myDict.pop(key)
#6. myDict.update(newDict)    - insertd  the specified items to  the dictionary

student= {
    "name": "Radhe shayam",
    "class" : "10th",
    "score" :{
        "chem":78,
        "phy":90,
        "math": 85,
        "Bio":78,
    
    } 
    
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("class"))
print(student.get("score"))