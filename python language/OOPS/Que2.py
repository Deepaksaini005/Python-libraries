#Create account class with 2 attributes - balance and accounnt no. create methods for debit ,credit and printing the balance .

class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc
        
        #debit method 
        
    def debit(self, amount):
         self.balance -= amount
         print("Debited amount is ", amount)
         print("Total balance = " , self.get_balance())
         
         
           # credit method
             
    def credit(self, amount):
         self.balance += amount
         print("credited amount is ", amount)
         
    def get_balance(self):
        return self.balance
         
         
acc1=Account(100000 ,4563792) 
print("account_no.is:" ,acc1.account_no)
acc1.debit(5000)
acc1.credit(10000)

   