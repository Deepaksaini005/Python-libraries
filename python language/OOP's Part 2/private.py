class Account:
    def __init__(self ,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass    #here we are using double underscore to make it private variable
    
    def reset_pass(self):
        print(self.__acc_pass)  # here we are accessing private variable using self keyword
    
acc1 = Account("845783293729","pdbg@34")
print(acc1.reset_pass())
        
    