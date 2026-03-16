import seaborn as sns 
import pandas  as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


gap= px.data.gapminder()
print(gap)

data = gap.loc[gap["country"]=="India"]
print(data)


# ye h axis  level pr jo ye plot banya h 
sns.lineplot(data = data , x = "year" , y = "pop" )


# ab figure level
sns.relplot(data = data , x = "year" , y = "pop" )
plt.show()


# Brazil , Germany , India


gap = px.data.gapminder()

data = gap.loc[gap["country"] == "India"]
data1 = gap.loc[gap["country"] == "Brazil"]
data2 = gap.loc[gap["country"] == "Germany"]

countries = pd.concat([data, data1, data2])

# Figure-level plot
sns.relplot(data=countries,x="year",y="pop",kind="line",hue="country"
)

plt.show()
