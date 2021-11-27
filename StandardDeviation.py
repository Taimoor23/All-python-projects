import math
import csv
with open('C:/Users/Bajwa/Downloads/data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
new_data=file_data[0]    
def mean (new_data):
    n=len(new_data)
    total=0
    for x in new_data:
        total=total+int(x)
    mean=total/n
    return mean        
squared_list=[]    
for number in new_data:
    a=int(number)-mean(new_data)
    a=a**2
    squared_list.append(a)
sum=0
for i in squared_list:
    sum=sum+i
result=sum/(len(new_data)-1)        
sd=math.sqrt(result)
print('The Standard Deviation is:',sd)
