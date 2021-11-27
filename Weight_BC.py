import pandas as pd
import csv 
import plotly_express as px
import plotly.figure_factory as ff 
df=pd.read_csv('C:/Users/Bajwa/Downloads/.csv')
fig=ff.create_distplot([df['Weight(Pounds)'].tolist()],['Weight'],show_hist=False)
fig.show()