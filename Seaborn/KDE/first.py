import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# KDE  - KDE batata hai data zyada kaha concentrated hai aur kaha kam, bina bars (histogram) ke. 

Employee_data = pd.DataFrame({
    'Employee_ID' :np.random.randint(1 , 100 , size = 50) ,
    'Age' : np.random.randint(22 , 60 , size = 50),
    'Salary' : np.random.randint(30000 , 120000 , size = 50),
    'Department' : np.random.choice(['HR', 'Finance', 'IT', 'Marketing', 'Sales']),
    'Gender' : np.random.choice(['Male', 'Female'] , size = 50),
    'Experience': np.random.randint(1 , 40 , size = 50),  
    'Performance' :np.random.choice(['Excellent', 'Good', 'Average', 'Poor'] , size = 50)
})

sns.histplot(data = Employee_data , x =  "Age" ,  kde=True)
sns.set_theme(font_scale=1.2)


sns.barplot(data = Employee_data ,  x = "Department" , y = "Salary" ,hue = "Gender" , estimator=np.sum)
plt.title("Salary vs Department and Gender")
plt.show()

def percentile():
    return np.percentile 

sns.barplot(data = Employee_data ,  x = "Department" , y = "Salary" ,hue = "Gender" )
plt.show()