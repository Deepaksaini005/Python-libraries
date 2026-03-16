import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dataset for an Employee  with random module - employe_id ,  age, salary, department , gender , experience , performance 

employee_id = np.random.randint(1 , 100 , size = 50)

age = np.random.randint(22 , 60 , size = 50)

salary = np.random.randint(30000 , 120000 , size = 50)

departments = ['HR', 'Finance', 'IT', 'Marketing', 'Sales']

department = np.random.choice(departments , size = 50)

gender = np.random.choice(['Male', 'Female'] , size = 50)

experience = np.random.randint(1 , 40 , size = 50) 
 
performance = np.random.choice(['Excellent', 'Good', 'Average', 'Poor'] , size = 50)

# dataframe
Employee_data = pd.DataFrame({
    'Employee_ID' : employee_id,
    'Age' : age,
    'Salary' : salary,
    'Department' : department,
    'Gender' : gender,
    'Experience' : experience,  
    'Performance' : performance
})
print(Employee_data)

print(sns.get_dataset_names())
penguins = sns.load_dataset('penguins')
print(penguins.head())

print(penguins["species"].value_counts())

# sns.scatterplot(data = penguins , x = 'flipper_length_mm' , y = "body_mass_g" , hue = 'species')

sns.scatterplot(data =Employee_data , x = "Age" , y ="Salary" , hue = "Gender")  
plt.show()