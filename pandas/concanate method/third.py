import  pandas as pd 

std = pd.read_csv(r"C:\Users\saini\Downloads\students.csv")
reg1 = pd.read_csv(r"C:\Users\saini\Downloads\reg-month1.csv")
reg2 =  pd.read_csv(r"C:\Users\saini\Downloads\reg-month2.csv")
courses = pd.read_csv(r"C:\Users\saini\Downloads\courses.csv")
deli = pd.read_csv(r"C:\Users\saini\Downloads\deliveries.csv")
matchs  = pd.read_csv(r"C:\Users\saini\Downloads\matches.csv")

regs =pd.concat([reg1 , reg2] , ignore_index=True)
print(regs)

regs1 =pd.concat([reg1 , reg2] , keys = ["reg1" , "reg2"], axis = 1)
print(regs1)


