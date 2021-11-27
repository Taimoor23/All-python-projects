import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import csv
df=pd.read_csv('C:/Users/Bajwa/Downloads/data4.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()],['Avg Rating'])
fig.show()