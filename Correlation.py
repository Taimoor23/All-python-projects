import plotly_express as px 
import csv
import numpy as np
def getDataSource(data_path):
    marks_percentage=[]
    days_present=[]
    with open(data_path)as f:
        # this will read the document in the form of dictionary
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            marks_percentage.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))
    return {'x':marks_percentage,'y':days_present}        
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])  
    print('The correlation between the marks in percentage and days present is:',correlation[0,1])  
def setUp():    
    data_path='C:/Users/Bajwa/Downloads/CSV_Files (2)/Student Marks vs Days Present.csv'
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setUp()    
