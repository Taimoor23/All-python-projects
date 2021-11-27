import pandas as pd
import plotly_express as px
df=pd.read_csv('C:/Users/Bajwa/Downloads/CSV_files/data.csv')
fig=px.scatter(df,x='Country',y='InternetUsers',color='color')
fig.show()