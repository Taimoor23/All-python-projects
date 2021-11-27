import plotly_express as px 
import csv
import numpy as np
def getDataSource(data_path):
    coffee_in_ml=[]
    sleep_in_hours=[]
    with open(data_path)as f:
        # this will read the document in the form of dictionary
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            coffee_in_ml.append(float(row['Coffee in ml']))
            sleep_in_hours.append(float(row['sleep in hours']))
    return {'x':coffee_in_ml,'y':sleep_in_hours}        
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])  
    print('The correlation between coffee in ml and sleep in hours is:',correlation[0,1])  
def setUp():    
    data_path='C:/Users/Bajwa/Downloads/CSV_Files (2)/cups of coffee vs hours of sleep.csv'
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setUp()    
