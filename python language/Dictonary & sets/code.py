# a= str(input("Enter the name :"))
# b= int(input("Enter the age :"))
# c= str(input("Enter the city :"))
# d= int(input("Enter the phone number :"))
# e= input("Enter the caste :")

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))


# a= eval(input("Enter the first no. :"))
# b= eval(input("Enter the second no. :"))
# c= eval(input("Enter the   third no.:"))
# d= eval(input("Enter the fourth no. :"))
# e =a+b+c+d
# print(e)


# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))



# list = [ 12 , "o" , 23.4 , True , 23j ]
# print(list)
# print(type(list))


# num = [1,2,3,4,5,["ok","a","f"],6,7,8,9]
# print(num)




# tup = ( 1,1.4 , "a", True , 23j )
# print(tup)
# print(type(tup))
# mylist = list(tup)
# print(mylist)
# mylist[2] = 4
# print(mylist) 
# mytup = tuple(mylist)
# print(mytup)



# mydict = {  "name":"Abhishek" ,
#   "age":25 ,
#   "city":"Bangalore",
#   "marks": [23,45,57,87], 
#   "gender" : "male",
  
# }

# print(mydict["marks"])





# dict = {  "name":"Abhishek" ,
#         "age":25 ,
#         "city":"Bangalore",
#        "score" :{
#            "maths": 90 ,
#            "science": 85 ,
#            "english": 95 ,
#        }

# }

# dict["score"]["english"] =45 
# print(dict)




# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {1,2,28,45,58,956,58,80}
# print(set1.intersection(set2))
# print(set1.union(set2))
# print(set1.difference(set2))
# print(set2.difference_update(set1))




# mydict["age"] = 30
# mydict["city"]="jaipur"
# print(mydict)


# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# print(list1 + list2)  



# tup1 = (1,2,3,4,5)
# tup2 = (6,7,8,9,10)
# print(tup1+tup2)  




# list  = [1,2,3,4,5]
# # print(3 in list)




# tup = (1,2,3,4,5)
# print(3 in tup)





# dic  = {"name":"Abhishek","age":25,"city":"Bangalore"}
# print("name" in dic)  





# key = ["a", "b", "c"]
# value = ["A","B" ,"C"]
# print(dict(zip(key,value)))





# age = int(input("Enter your age :"))
# if (age >=18 ):
#     print("You are able for  give vote")
# else:
#     print("not able  for vote ")





# marks = int(input("Enter your marks :"))
# if (marks >= 90):
#     print("Grade A")
# elif (marks >= 80):
#     print("Grage B")
# else :
#     print("Grade C")

  
  
  
  
# char = input("Enter a character :")
# if (char == "a" or char =="e"or char =="i" or char =="o" or char =="u"):
#     print("Vowel")
# else:
#     print("Consonant")
    
  
  
  
  #checkif a number is multiple of the 3 and 5 or both 

# num = int(input("Enter a number: "))

# if (num % 3 == 0) and (num % 5 == 0):
#     print("Number is a multiple of both 3 and 5")
# elif (num % 3 == 0):
#     print("Number is a multiple of 3")
# elif (num % 5 == 0):
#     print("Number is a multiple of 5")
# else:
#     print("Number is not a multiple of 3 or 5")






# Program to find the largest of three numbers


# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# num3 = eval(input("Enter the third number: "))
 
# if num1 > num2 and num1 > num3:
#     print(num1, "is the largest number")
# elif num2 > num1 and num2 > num3:
#     print(num2, "is the largest number")
# elif num3 > num1 and num3 > num2:
#     print(num3, "is the largest number")
# else:
#     print("Two or more numbers are equal")





# ch = input("Enter a single character: ")

# if len(ch) == 1:  
#     if (ch.islower()):
#         print("Lowercase letter")
#     elif (ch.isupper()):
#         print("Uppercase letter")
#     elif (ch.isdigit()):
#         print("Digit")
#     else:
#         print("Special character")
# else:
#     print("Please enter only one character.")




# marks = int(input("Enter the marks: "))
# if(marks >= 90):
#     print("Grade A ")
# elif(marks >= 80):
#     print("Grade B ")
# elif(marks >= 70):
#     print("Grade C ")
# else :
#   print("Fail ")



# side1 =  input("Enter the first side of the triangle: ")
# side2 = input("Enter the second side of the triangle: ")
# side3 = input("Enter the third side of the triangle: ")

# if (side1 ==side2 == side3):
#     print("The triangle is equilateral")
# elif (side1 == side2 or side2 ==side3 or side1==side3):
#     print("The triangle is isosceles")
# elif (side1 != side2 and side2 != side3 and side1 != side3):
#     print(" The triangle is scalene")
# else:
#     print(" Invalid input")





# angle1 = eval(input("Enter the first angle: "))
# angle2 = eval(input("Enter the second angle: "))
# angle3 = eval(input("Enter the third angle: "))

# if( angle1 + angle2 + angle3 == 180):
#     print("The angles are valid for a triangle")
# else:
#     print("Angles are not valid for a triangle")



# year = eval(input("Enter the year: "))

# if(year%100==0 ):
#     print(" The year is a century  year")
# else :
#     print("Year is not a century year")




# day = eval(input("Enter the day :"))
# if (day == 0):
#     print("Sunday")
# elif (day == 1):
#     print("monday")
# elif (day == 2):
#     print("tuesday")
# elif (day == 3):
#     print("Wednesday")
# elif (day == 4):
#     print("Thursday")
# elif (day == 5):
#     print("Friday")
# elif (day == 6):
#     print("saturday")
# else:
#     print("Invalid day")




# num = int(input( "Enter a num : "))

# if ( num >=100 and  num <=999 ):
#     print("Three digit number")
# elif (str(num) ==str(num)[::-1] ):
#     print(" Palindrome")
# else:
#     print(" Not a three digit number or not a palindrome")






# num = int(input("Enter a number: "))

# if (num>1 ):
#     for i in range(2,num):
#         if (num % i == 0):
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")
# else:
#     print(" Invalid input")