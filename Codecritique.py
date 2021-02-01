#Extract data as a dataframe from CSV.
import pandas as pd 
import numpy as np
data = pd.read_csv("CrashData_2019.csv") 
data.head(10)


#Every record should have VehicleID(As it is related to crash)

for item in enumerate(data['Vehicle ID']):
    #(0, nan),(1, 3409578.0),(2, 3409578.0)
    if(math.isnan(item[1])):
        num=len(data)-data['Vehicle ID'].count()
    else:
        pass
print("The number of invalid vehicle entries are",num)   #--508  



#Every record should have highway number as 26(As the crashes are on highway 26)

for item in enumerate(data['Highway Number']):
    #(0, 26.0)(1, nan)(2, nan)
    if(int(item[1]!=26)):
        num=len(data)-data['Highway Number'].count()
    else:
        pass

print("The number of invalid vehicle entries are",num)   #2231 



# Each record should have Distance from Intersection must = 0 when Road Character = 1
# And distance from Intersection > 0 when Road Character is not 1 (Intersection) and Milepoint is not provided.

count=0
count1=0
for dis in data['Distance from Intersection']:
    for road in data['Road Character']:
        for mile in data['Milepoint']:
            if(road==1 and dis==0):
                count+=1
            elif(road!=1 and dis>0 and math.isnan(mile)):
                 count1+=1       
            else:
                pass
print("Number of records which have Distance from Intersection as 0 when Road Character is 1 are",count)#0
print("Number of records which have Distance from Intersection greater than 0 when Road Character is not 1\
 and milepoint is not provided are",count1)#2231
 
 

#Every record should have Traffic Control Device as 0 or 1.
count=0
for item in enumerate(data['Traffic Control Device (TCD)']):
     if(int(item[1]==0) or int(item[1]==1)):
        count+=1
print("Number of records should have Traffic Control Device as 0 or 1 is ",count)


    
#Each record should have a unique CrashID.
import collections
collections.Counter(data['Crash ID'])# {1809119: 5,1809229: 4,1809637: 3,1810874: 4}    

#Combination of month, day and year should represent a valid date
year=data[data['Crash Year']==2019]
float_col = year.select_dtypes(include=['float64'])
float_col_list = list(float_col.columns.values)
for col in float_col_list:
    if(col in ignore):
        pass
    else:
        year[col] = year[col].astype('Int64')
date_format = DataFrame(year, columns= ['Crash Month', 'Crash Day','Crash Year'])
# print(date_format)
date_frame=date_format['Crash Month'].astype(str)+"-"+date_format['Crash Day'].astype(str)+"-"+date_format['Crash Year'].astype(str)
for i in date_frame:
    date_str=str(i)
    format = "%m-%d-%Y"
    if(datetime.datetime.strptime(date_str, format)):
        print("valid date")
    else:
        print("invalid")
		
#Every record should have participant ID for corresponding vehicle ID
small = DataFrame(data, columns= ['Crash ID', 'Participant ID'])
count=0
for item in enumerate(small['Participant ID']):
    if(math.isnan(item[1])):
        pass
    else:
        for crash in small['Crash ID']:
            if(math.isnan(crash)):
                pass
            else:
                count+=1
print("Number of records which have participant ID for corresponding vehicle ID are",count)#1216