import plotly_express as px
import csv
import numpy as np 

with open('C:/Users/Bajwa/Downloads/CSV_Files (2)/cups of coffee vs hours of sleep.csv') as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x='sleep in hours', y='Coffee in ml',size_max=100)
    fig.show()
