import pandas as pd
import csv
import plotly.graph_objects as go
import plotly_express as px
df=pd.read_csv('C:/Users/Bajwa/Downloads/data2.csv')
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(mean.groupby('level')['attempt'].mean())
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()