import pandas as pd
import csv 
import plotly_express as px
import plotly.figure_factory as ff 
df=pd.read_csv('C:/Users/Bajwa/Downloads/data3.csv')
fig=ff.create_distplot([df['Height(Inches)'].tolist()],['Height'],show_hist=False)
fig.show()