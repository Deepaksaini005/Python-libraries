import seaborn as sns 
import pandas  as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

tip= sns.load_dataset("tips")
print(tip)

sns.scatterplot(data = tip , x  = "total_bill" , y = "tip" ,  hue= "sex" ,  size = "size" , style = "time" )

# difference b/w the scaatter and the relplot is scatter comes  inside the rectngle and the relplot are  made in the angle plot type

sns.relplot(data = tip , x  = "total_bill" , y = "tip" ,  hue= "sex" ,  size = "size" , style = "time")

plt.show()

gap= px.data.gapminder() #gapminder data set ko load krne ke liye
print(gap)
