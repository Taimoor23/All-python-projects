import pandas as pd
import plotly_express as px 
df=pd.read_csv('C:/Users/Bajwa/OneDrive/Documents/Book1.xlsx')
fig=px.line(df , x='Kindness',y='freedom',color='Names')
fig.show()