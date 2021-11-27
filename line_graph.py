import pandas as pd
import plotly_express as px 
df=pd.read_csv('C:/Users/Bajwa/Downloads/CSV_files/line_chart.csv')
fig=px.line(df , x='Year',y='Per capita income',color='Country',title='Per Capita Income')
fig.show()