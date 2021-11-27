import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import csv
import random
import statistics
df=pd.read_csv('C:/Users/Bajwa/Downloads/Newdata.csv')
data=df['average'].tolist()
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)    
    return mean
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],['average'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,12],mode='lines',name='mean'))
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print('mean of sample distribution:',mean)
setup()    

def std():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    mean=statistics.stdev(mean_list)
    print('mean of sample distribution:',mean)
std()    
population_mean=statistics.mean(data)
print('population of the mean:',population_mean)

population_std=statistics.stdev(data)
print('population of standard deviation:',population_std)