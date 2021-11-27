import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics as st
import random
import numpy

df=pd.read_csv('C:/Users/Bajwa/Downloads/CSV_files/School2.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([data],['Math Score'],show_hist=False)
fig.show()
mean_1=st.mean(data)
std_deviation=st.stdev(data)
print('the mean is:',mean_1)
print('the st deviatation is:',std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=st.mean(dataset)    
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)
mean=st.mean(mean_list)
print('mean of sample distrib:',mean) 
std_deviation=st.stdev(mean_list) 
print('sd of smaple distrib:',std_deviation)
fig_1=ff.create_distplot([mean_list],['Mean List'],show_hist=False)
fig_1.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode='lines',name='Mean'))
fig_1.show()
first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
print('std1:',first_std_deviation_start,first_std_deviation_end)
print('std2:',second_std_deviation_start,second_std_deviation_end)
print('std3:',third_std_deviation_start,third_std_deviation_end)
fig_2=ff.create_distplot([mean_list],['Student marks'],show_hist=False)
fig_2.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
fig_2.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig_2.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig_2.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig_2.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig_2.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 3'))
fig_2.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 3'))
fig_2.show()
dtf=pd.read_csv('C:/Users/Bajwa/Downloads/CSV_files/School_1_sample.csv')
data_1=dtf['Math_score'].tolist()
meanofsample1=st.mean(data_1)
print('mean of the 1st solution is:',meanofsample1)
fig_2=ff.create_distplot([mean_list],['Student marks'],show_hist=False)
fig_2.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
fig_2.add_trace(go.Scatter(x=[meanofsample1,meanofsample1],y=[0,0.17],mode='lines',name='Mean'))
fig_2.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig_2.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig_2.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig_2.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig_2.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 3'))
fig_2.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 3'))
fig_2.show()
dtf_2=pd.read_csv('C:/Users/Bajwa/Downloads/CSV_files/School_2_Sample.csv')
data_2=dtf_2['Math_score'].tolist()
meanofsample2=st.mean(data_2)
print('mean of the 2nd solution is:',meanofsample2)
fig_2=ff.create_distplot([mean_list],['Student marks'],show_hist=False)
fig_2.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
fig_2.add_trace(go.Scatter(x=[meanofsample2,meanofsample2],y=[0,0.17],mode='lines',name='Mean of sample 2'))
fig_2.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig_2.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig_2.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig_2.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig_2.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 3'))
fig_2.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 3'))
fig_2.show()
dtf_3=pd.read_csv('C:/Users/Bajwa/Downloads/CSV_files/School_3_Sample.csv')
data_3=dtf_3['Math_score'].tolist()
meanofsample3=st.mean(data_3)
print('mean of the 2nd solution is:',meanofsample3)
fig_2=ff.create_distplot([mean_list],['Student marks'],show_hist=False)
fig_2.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
fig_2.add_trace(go.Scatter(x=[meanofsample3,meanofsample3],y=[0,0.17],mode='lines',name='Mean of sample 3'))
fig_2.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig_2.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig_2.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig_2.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig_2.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 3'))
fig_2.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 3'))
fig_2.show()

z_score=(mean-meanofsample2)/std_deviation
print('the z score is:',z_score)