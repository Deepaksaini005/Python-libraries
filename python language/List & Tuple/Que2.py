#WAP to check if a list contains a palindrome of the elements .
#plaindrome- : same as front and end 

word = input("Enter a word: ")  # Take input from user
list1 = list(word)

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("Palindrome")
else:
    print("Not a Palindrome")



