
import pandas as pd
a = {
  "Name": [ "John", "Jane", "Doe" ],
  "Age": [ 28, 34, 29 ],
  "City": [ "New York", "Los Angeles", "Chicago" ],
   "Role": [ "Engineer", "Designer", "Manager" ],
   "Birth_Year": [ 1995, 1990, 1985 ]
}

df = pd.DataFrame(a , index=["A", "B", "C"])
print(df.loc["A"]["Name"])  #accessing the value of the name column at index 0.



# by using simple method .

df = pd.DataFrame(a)
print(df["Name"][0])


# using the ilock method

df = pd.DataFrame(a)
print(df.iloc[0])  

# accessing multiple rows by using iloc method

df = pd.DataFrame(a , index=["A", "B", "C"])
print(df.iloc[[0 ,2 ,1]])


#access the multiple rows by the slicing method  using  iloc  method.  
df = pd.DataFrame(a , index=["A", "B", "C"])
print(df.iloc[0:2 ,1: 4])  # accessing rows from index 0 to 2 and columns from index 1 to 4


df = pd.DataFrame(a , index=["A", "B", "C"])
print(df.iloc[:, [1,3]])  # accesing rows  with integer psoition .



df =  pd.DataFrame(a , index=["A", "B", "C"])
print(df.iloc[[0,2] , [1,3]])


#using negative index 

df =  pd.DataFrame(a , index=["A", "B", "C"])
print(df.iloc[-3]["Birth_Year"]) 
