import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
mean=sum(dice_result)/len(dice_result)    
median=st.median(dice_result)
mode=st.mode(dice_result)
std_deviation=st.stdev(dice_result)
first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
fig=ff.create_distplot([dice_result],['result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 1'))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name='Standard deviation 2'))
fig.show()
list_of_data_within_one_standard_deviation=[result for result in dice_result if result>first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_two_standard_deviation=[result for result in dice_result if result>second_std_deviation_start and result<second_std_deviation_end]
list_of_data_within_three_standard_deviation=[result for result in dice_result if result>third_std_deviation_start and result<third_std_deviation_end]
print('Mean of this data is {}'.format(mean))
print('Median of this data is {}'.format(median))
print('Mode of this data is {}'.format(mode))
print('Standard deviation of this data is {}'.format(std_deviation))
print('{}% of data lies within one standard deviation'.format(len(list_of_data_within_one_standard_deviation)*100.0/len(dice_result)))
print('{}% of data lies within two standard deviation'.format(len(list_of_data_within_two_standard_deviation)*100.0/len(dice_result)))
print('{}% of data lies within three standard deviation'.format(len(list_of_data_within_three_standard_deviation)*100.0/len(dice_result)))
