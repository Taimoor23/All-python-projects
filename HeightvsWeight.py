import statistics
import pandas as pd
import csv

df = pd.read_csv("C:/Users/Bajwa/Downloads/StudentsPerformance.csv")
m_list = df["math score"].to_list()
m_mean = statistics.mean(m_list)
m_median = statistics.median(m_list)
m_mode = statistics.mode(m_list)

print("Mean, Median and Mode of math score is {}, {} and {} respectively".format(m_mean,m_median,m_mode))

m_sd = statistics.stdev(m_list)
m_first_sd_start, m_first_sd_end = m_mean-m_sd, m_mean+m_sd
m_second_sd_start, m_second_sd_end = m_mean-m_sd*2, m_mean+m_sd*2
m_third_sd_start, m_third_sd_end = m_mean-m_sd*3, m_mean+m_sd*3

m_data_within_first_sd = [result for result in m_list if result> m_first_sd_start and result< m_first_sd_end]
m_data_within_second_sd = [result for result in m_list if result> m_second_sd_start and result< m_second_sd_end]
m_data_within_third_sd = [result for result in m_list if result> m_third_sd_start and result< m_third_sd_end]
print("{}% of data for math score lies between first standered deviation".format(len(m_data_within_first_sd)*100/len(m_list)))
print("{}% of data for math score lies between second standered deviation".format(len(m_data_within_second_sd)*100/len(m_list)))
print("{}% of data for math score lies between third standered deviation".format(len(m_data_within_third_sd)*100/len(m_list)))

r_list = df["reading score"].to_list()
r_mean = statistics.mean(r_list)
r_median = statistics.median(r_list)
r_mode = statistics.mode(r_list)

print("Mean, Median and Mode of reading score is {}, {} and {} respectively".format(r_mean,r_median,r_mode))

r_sd = statistics.stdev(r_list)
r_first_sd_start, r_first_sd_end = r_mean-r_sd, r_mean+r_sd
r_second_sd_start, r_second_sd_end = r_mean-r_sd*2, r_mean+r_sd*2
r_third_sd_start, r_third_sd_end = r_mean-r_sd*3, r_mean+r_sd*3

r_data_within_first_sd = [result for result in r_list if result> r_first_sd_start and result< r_first_sd_end]
r_data_within_second_sd = [result for result in r_list if result> r_second_sd_start and result< r_second_sd_end]
r_data_within_third_sd = [result for result in r_list if result> r_third_sd_start and result< r_third_sd_end]
print("{}% of data for reading score lies between first standered deviation".format(len(r_data_within_first_sd)*100/len(r_list)))
print("{}% of data for reading score lies between second standered deviation".format(len(r_data_within_second_sd)*100/len(r_list)))
print("{}% of data for reading score lies between third standered deviation".format(len(r_data_within_third_sd)*100/len(r_list)))

w_list = df["writing score"].to_list()
w_mean = statistics.mean(w_list)
w_median = statistics.median(w_list)
w_mode = statistics.mode(w_list)

print("Mean, Median and Mode of writing score is {}, {} and {} respectively".format(w_mean,w_median,w_mode))

w_sd = statistics.stdev(w_list)
w_first_sd_start, w_first_sd_end = w_mean-w_sd, w_mean+w_sd
w_second_sd_start, w_second_sd_end = w_mean-w_sd*2, w_mean+w_sd*2
w_third_sd_start, w_third_sd_end = w_mean-w_sd*3, w_mean+w_sd*3

w_data_within_first_sd = [result for result in w_list if result> w_first_sd_start and result< w_first_sd_end]
w_data_within_second_sd = [result for result in w_list if result> w_second_sd_start and result< w_second_sd_end]
w_data_within_third_sd = [result for result in w_list if result> w_third_sd_start and result< w_third_sd_end]
print("{}% of data for writing score lies between first standered deviation".format(len(w_data_within_first_sd)*100/len(w_list)))
print("{}% of data for writing score lies between second standered deviation".format(len(w_data_within_second_sd)*100/len(w_list)))
print("{}% of data for writing score lies between third standered deviation".format(len(w_data_within_third_sd)*100/len(w_list)))