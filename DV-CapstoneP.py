import pandas as pd 
import plotly_express as px 
df= pd.read_csv('C:/Users/Bajwa/Downloads/Copy+of+data+-+data.csv')
fig=px.scatter(df,x='date',y='cases',color='country')
fig.show()