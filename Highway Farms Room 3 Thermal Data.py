#!/usr/bin/env python
# coding: utf-8

# Script for processing Highway Farms Environment data for Room 3
# This code along with the stats compiler code added at the end of the file are intended to automate reading in all pertinent raw 
#data files for each individual sensor and a file of the farrow and wean dates accosiated with the sensor pods. 
#The code then selects the correct date range, downsamples to a 5 minute interval on the mean method, convert Farenheit values to celeus, 
#joins the individual sensors into a data frame for each pod. Calculations for the mean radiant temperature are performed where necessary 
#with the correct values for ball diameter. Summary statistics are performed for each sensor pod and outputed. The last section of the 
#code is what compiles all the stats into a single file to be used to create graphs for a publication.
# Further work includes duplicating this script and customizing it to the Room 4 sensor setup that is very different from this room.
# 

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime


# In[3]:


#goal is to read in a set of dates from another file to then assign to a variable and 
#automate switching between turns of data
df = pd.read_excel('Dates.xlsx', sheet_name='Sheet1')
#df.head()
#df.info()
fd1 = df['Farrow Date']
H1fd=fd1[0]
H2fd =fd1[1]
H3fd=fd1[2]
H4fd=fd1[3]
H5fd=fd1[4]
H6fd=fd1[5]
HL1fd=fd1[12]
HL2fd=fd1[13]
HL3fd=fd1[14]
RM3fd=fd1[18]

#Set Wean date
wd1 = df['Wean Date']
H1wd=wd1[0]
H2wd =wd1[1]
H3wd=wd1[2]
H4wd=wd1[3]
H5wd=wd1[4]
H6wd=wd1[5]
HL1wd=wd1[12]
HL2wd=wd1[13]
HL3wd=wd1[14]
RM3wd=wd1[18]
H1wd


# In[2]:


#Read in Raw Data 
series1 = pd.read_csv("H1DB.csv")
series2 = pd.read_csv("H1G.csv")
series3 = pd.read_csv("H1RH.csv")
#series1.head()
#series2.head()
#series3.head()

series4 = pd.read_csv("H2DB.csv")
series5 = pd.read_csv("H2G.csv")
series6 = pd.read_csv("H2RH.csv")

series7 = pd.read_csv("H3DB.csv")

series8 = pd.read_csv("H4DB.csv")
series9 = pd.read_csv("H4G.csv")
series10 = pd.read_csv("H4RH.csv")

series11 = pd.read_csv("H5DB.csv")
series12 = pd.read_csv("H5G.csv")
series13 = pd.read_csv("H5RH.csv")

series14 = pd.read_csv("H6DB.csv")

series15 = pd.read_csv("L1DB.csv")
series16 = pd.read_csv("L1G.csv")
#series17 = pd.read_csv("L1RH.csv") not in turn 1

series18 = pd.read_csv("L2DB.csv")
series19 = pd.read_csv("L2G.csv")
series20 = pd.read_csv("L2RH.csv")

series21 = pd.read_csv("L3DB.csv")
series22 = pd.read_csv("L3G.csv")

series23 = pd.read_csv("R3DB1.csv")
series24 = pd.read_csv("R3DB2.csv")
series25 = pd.read_csv("R3RH1.csv")
series26 = pd.read_csv("R3RH2.csv")


# In[3]:


# Trim by date, down sample to 5 minute interval Haven 1
H1Tdata=series1.set_index(pd.DatetimeIndex(series1.Date))[H1fd:H1wd]
fminH1DB=H1Tdata.resample('5T').mean()
#fminH1DB.head()
H1DB = fminH1DB.copy()
H1DB['Value'] = fminH1DB['Value'].fillna(fminH1DB['Value'].mean())
H1DB.columns = ['Tdbf']
H1DB.head()
H1Gdata=series2.set_index(pd.DatetimeIndex(series2.Date))[H1fd:H1wd]
fminH1G=H1Gdata.resample('5T').mean()
#fminH1G.head()
H1G = fminH1G.copy()
H1G['Value'] = fminH1G['Value'].fillna(fminH1G['Value'].mean())
H1G.columns = ['Tgf']
#print(H1G)
H1RHdata=series3.set_index(pd.DatetimeIndex(series3.Date))[H1fd:H1wd]
fminH1RH=H1RHdata.resample('5T').mean()
H1RH = fminH1RH.copy()
H1RH['Value'] = fminH1RH['Value'].fillna(fminH1RH['Value'].mean())
H1RH.columns = ['RH%']
#H1RH.head()


# In[4]:


# Haven 2
H2Tdata=series4.set_index(pd.DatetimeIndex(series4.Date))[H2fd:H2wd]
fminH2DB=H2Tdata.resample('5T').mean()
#fminH1DB.head()
H2DB = fminH2DB.copy()
H2DB['Value'] = fminH2DB['Value'].fillna(fminH2DB['Value'].mean())
H2DB.columns = ['Tdbf']
#H2DB.head()
H2Gdata=series5.set_index(pd.DatetimeIndex(series5.Date))[H2fd:H2wd]
fminH2G=H2Gdata.resample('5T').mean()
#fminH1G.head()
H2G = fminH2G.copy()
H2G['Value'] = fminH2G['Value'].fillna(fminH2G['Value'].mean())
H2G.columns = ['Tgf']
#print(H1G)
H2RHdata=series6.set_index(pd.DatetimeIndex(series6.Date))[H2fd:H2wd]
fminH2RH=H2RHdata.resample('5T').mean()
H2RH = fminH2RH.copy()
H2RH['Value'] = fminH2RH['Value'].fillna(fminH2RH['Value'].mean())
H2RH.columns = ['RH%']
#H1RH.head()


# In[5]:


#Haven 3 and 6 just Dry bulb
H3Tdata=series7.set_index(pd.DatetimeIndex(series7.Date))[H3fd:H3wd]
fminH3DB=H3Tdata.resample('5T').mean()
#fminH1DB.head()
H3 = fminH3DB.copy()
H3['Value'] = fminH3DB['Value'].fillna(fminH3DB['Value'].mean())
H3.columns = ['Tdbf']

#Haven 6
H6Tdata=series14.set_index(pd.DatetimeIndex(series14.Date))[H6fd:H6wd]
fminH6DB=H6Tdata.resample('5T').mean()
#fminH1DB.head()
H6 = fminH6DB.copy()
H6['Value'] = fminH6DB['Value'].fillna(fminH6DB['Value'].mean())
H6.columns = ['Tdbf']


# In[6]:


# Haven 4
H4Tdata=series8.set_index(pd.DatetimeIndex(series8.Date))[H4fd:H4wd]
fminH4DB=H4Tdata.resample('5T').mean()
#fminH1DB.head()
H4DB = fminH4DB.copy()
H4DB['Value'] = fminH4DB['Value'].fillna(fminH4DB['Value'].mean())
H4DB.columns = ['Tdbf']
#H2DB.head()
H4Gdata=series9.set_index(pd.DatetimeIndex(series9.Date))[H4fd:H4wd]
fminH4G=H4Gdata.resample('5T').mean()
#fminH1G.head()
H4G = fminH4G.copy()
H4G['Value'] = fminH4G['Value'].fillna(fminH4G['Value'].mean())
H4G.columns = ['Tgf']
#print(H1G)
H4RHdata=series10.set_index(pd.DatetimeIndex(series10.Date))[H4fd:H4wd]
fminH4RH=H4RHdata.resample('5T').mean()
H4RH = fminH4RH.copy()
H4RH['Value'] = fminH4RH['Value'].fillna(fminH4RH['Value'].mean())
H4RH.columns = ['RH%']
#H1RH.head()


# In[7]:


#Haven 5
H5Tdata=series11.set_index(pd.DatetimeIndex(series11.Date))[H5fd:H5wd]
fminH5DB=H5Tdata.resample('5T').mean()
#fminH1DB.head()
H5DB = fminH5DB.copy()
H5DB['Value'] = fminH5DB['Value'].fillna(fminH5DB['Value'].mean())
H5DB.columns = ['Tdbf']
#H2DB.head()
H5Gdata=series12.set_index(pd.DatetimeIndex(series12.Date))[H5fd:H5wd]
fminH5G=H5Gdata.resample('5T').mean()
#fminH1G.head()
H5G = fminH5G.copy()
H5G['Value'] = fminH5G['Value'].fillna(fminH5G['Value'].mean())
H5G.columns = ['Tgf']
#print(H1G)
H5RHdata=series13.set_index(pd.DatetimeIndex(series13.Date))[H5fd:H5wd]
fminH5RH=H5RHdata.resample('5T').mean()
H5RH = fminH5RH.copy()
H5RH['Value'] = fminH5RH['Value'].fillna(fminH5RH['Value'].mean())
H5RH.columns = ['RH%']
#H1RH.head()


# In[8]:


# HL 1
HL1Tdata=series15.set_index(pd.DatetimeIndex(series15.Date))[HL1fd:HL1wd]
fminHL1DB=HL1Tdata.resample('5T').mean()
#fminH1DB.head()
HL1DB = fminHL1DB.copy()
HL1DB['Value'] = fminHL1DB['Value'].fillna(fminHL1DB['Value'].mean())
HL1DB.columns = ['Tdbf']
#H2DB.head()
HL1Gdata=series16.set_index(pd.DatetimeIndex(series16.Date))[HL1fd:HL1wd]
fminHL1G=HL1Gdata.resample('5T').mean()
#fminH1G.head()
HL1G = fminHL1G.copy()
HL1G['Value'] = fminHL1G['Value'].fillna(fminHL1G['Value'].mean())
HL1G.columns = ['Tgf']
#print(H1G)
#HL1RHdata=series17.set_index(pd.DatetimeIndex(series17.Date))[HL1fd:HL1wd]
#fminHL1RH=HL1RHdata.resample('5T').mean()
#HL1RH = fminHL1RH.copy()
#HL1RH['Value'] = fminHL1RH['Value'].fillna(fminHL1RH['Value'].mean())
#HL1RH.columns = ['RH%']
#H1RH.head()


# In[9]:


#HL 2
HL2Tdata=series18.set_index(pd.DatetimeIndex(series18.Date))[HL2fd:HL2wd]
fminHL2DB=HL2Tdata.resample('5T').mean()
#fminH1DB.head()
HL2DB = fminHL2DB.copy()
HL2DB['Value'] = fminHL2DB['Value'].fillna(fminHL2DB['Value'].mean())
HL2DB.columns = ['Tdbf']
#H2DB.head()
HL2Gdata=series19.set_index(pd.DatetimeIndex(series19.Date))[HL2fd:HL2wd]
fminHL2G=HL2Gdata.resample('5T').mean()
#fminH1G.head()
HL2G = fminHL2G.copy()
HL2G['Value'] = fminHL2G['Value'].fillna(fminHL2G['Value'].mean())
HL2G.columns = ['Tgf']
#print(H1G)
HL2RHdata=series20.set_index(pd.DatetimeIndex(series20.Date))[HL2fd:HL2wd]
fminHL2RH=HL2RHdata.resample('5T').mean()
HL2RH = fminHL2RH.copy()
HL2RH['Value'] = fminHL2RH['Value'].fillna(fminHL2RH['Value'].mean())
HL2RH.columns = ['RH%']
#H1RH.head()


# In[10]:


#HL3
HL3Tdata=series21.set_index(pd.DatetimeIndex(series21.Date))[HL3fd:HL3wd]
fminHL3DB=HL3Tdata.resample('5T').mean()
#fminH1DB.head()
HL3DB = fminHL3DB.copy()
HL3DB['Value'] = fminHL3DB['Value'].fillna(fminHL3DB['Value'].mean())
HL3DB.columns = ['Tdbf']
#H2DB.head()
HL3Gdata=series22.set_index(pd.DatetimeIndex(series22.Date))[HL3fd:HL3wd]
fminHL3G=HL3Gdata.resample('5T').mean()
#fminH1G.head()
HL3G = fminHL3G.copy()
HL3G['Value'] = fminHL3G['Value'].fillna(fminHL3G['Value'].mean())
HL3G.columns = ['Tgf']
#print(H1G)


# In[11]:


# Room Level Sensors
#DB1
RM3T1data=series23.set_index(pd.DatetimeIndex(series23.Date))[RM3fd:RM3wd]
fminRM3DB1=RM3T1data.resample('5T').mean()
RM3DB1 = fminRM3DB1.copy()
RM3DB1['Value'] = fminRM3DB1['Value'].fillna(fminRM3DB1['Value'].mean())
RM3DB1.columns = ['Tdbf1']
#DB2
RM3T2data=series24.set_index(pd.DatetimeIndex(series24.Date))[RM3fd:RM3wd]
fminRM3DB2=RM3T2data.resample('5T').mean()
RM3DB2 = fminRM3DB2.copy()
RM3DB2['Value'] = fminRM3DB2['Value'].fillna(fminRM3DB2['Value'].mean())
RM3DB2.columns = ['Tdbf2']
#RH1
RM3RH1data=series25.set_index(pd.DatetimeIndex(series25.Date))[RM3fd:RM3wd]
fminRM3RH1=RM3RH1data.resample('5T').mean()
RM3RH1 = fminRM3RH1.copy()
RM3RH1['Value'] = fminRM3RH1['Value'].fillna(fminRM3RH1['Value'].mean())
RM3RH1.columns = ['RH1']
#RH2
RM3RH2data=series26.set_index(pd.DatetimeIndex(series26.Date))[RM3fd:RM3wd]
fminRM3RH2=RM3RH2data.resample('5T').mean()
RM3RH2 = fminRM3RH2.copy()
RM3RH2['Value'] = fminRM3RH2['Value'].fillna(fminRM3RH2['Value'].mean())
RM3RH2.columns = ['RH2']


# In[12]:


# convert Temperature data from F to C
# Haven 1
H1DB['Tdbc']= (H1DB['Tdbf']-32)*(5/9)
#H1DB.head()
H1G['Tgc']= (H1G['Tgf']-32)*(5/9)
#print(H1DB)
#Haven 2
H2DB['Tdbc']= (H2DB['Tdbf']-32)*(5/9)
H2DB.head()
H2G['Tgc']= (H2G['Tgf']-32)*(5/9)
#Haven 3
H3['Tdbc']= (H3['Tdbf']-32)*(5/9)
#Haven 6
H6['Tdbc']= (H6['Tdbf']-32)*(5/9)
#Haven 4
H4DB['Tdbc']= (H4DB['Tdbf']-32)*(5/9)
H4G['Tgc']= (H4G['Tgf']-32)*(5/9)
#Haven 5
H5DB['Tdbc']= (H5DB['Tdbf']-32)*(5/9)
H5G['Tgc']= (H5G['Tgf']-32)*(5/9)
#HL1
HL1DB['Tdbc']= (HL1DB['Tdbf']-32)*(5/9)
HL1G['Tgc']= (HL1G['Tgf']-32)*(5/9)
#HL2
HL2DB['Tdbc']= (HL2DB['Tdbf']-32)*(5/9)
HL2G['Tgc']= (HL2G['Tgf']-32)*(5/9)
#HL3 
HL3DB['Tdbc']= (HL3DB['Tdbf']-32)*(5/9)
HL3G['Tgc']= (HL3G['Tgf']-32)*(5/9)
#Room Sensors
RM3DB1['Tdbc1']= (RM3DB1['Tdbf1']-32)*(5/9)
RM3DB2['Tdbc2']= (RM3DB2['Tdbf2']-32)*(5/9)


# In[13]:


#join data for the pods together
#Haven 1
H1a = pd.merge(left=H1DB, right=H1G, how='left', left_on='Date', right_on='Date')
#H1.head()
H1 = pd.merge(left=H1a, right=H1RH, how ='left', left_on='Date',right_on='Date')
H1.head()
#Haven 2
H2a = pd.merge(left=H2DB, right=H2G, how='left', left_on='Date', right_on='Date')
#H1.head()
H2 = pd.merge(left=H2a, right=H2RH, how ='left', left_on='Date',right_on='Date')
H2.head()
#Haven 4
H4a = pd.merge(left=H4DB, right=H4G, how='left', left_on='Date', right_on='Date')
#H1.head()
H4 = pd.merge(left=H4a, right=H4RH, how ='left', left_on='Date',right_on='Date')
#H4.head()
#Haven 5
H5a = pd.merge(left=H5DB, right=H5G, how='left', left_on='Date', right_on='Date')
#H1.head()
H5 = pd.merge(left=H5a, right=H5RH, how ='left', left_on='Date',right_on='Date')
#H4.head()
#HL1
HL1 = pd.merge(left=HL1DB, right=HL1G, how='left', left_on='Date', right_on='Date')
#H1.head()
#HL1 = pd.merge(left=HL1a, right=HL1RH, how ='left', left_on='Date',right_on='Date')
#HL2
HL2a = pd.merge(left=HL2DB, right=HL2G, how='left', left_on='Date', right_on='Date')
#H1.head()
HL2 = pd.merge(left=HL2a, right=HL2RH, how ='left', left_on='Date',right_on='Date')
#HL3
HL3 = pd.merge(left=HL3DB, right=HL3G, how='left', left_on='Date', right_on='Date')
#Room Sensors
RM3a = pd.merge(left=RM3DB1, right=RM3DB2, how='left', left_on='Date', right_on='Date')
#H1.head()
RM3b = pd.merge(left=RM3a, right=RM3RH1, how ='left', left_on='Date',right_on='Date')
RM3 = pd.merge(left=RM3b, right=RM3RH2, how ='left', left_on='Date',right_on='Date')


# In[14]:


# Calculate the Tmr value
#Haven 1
H1['Tmrc']=((((H1['Tgc']+273)**4)+((0.25*(10**8))/0.95)*(((abs(H1['Tgc']-H1['Tdbc']))/0.051)**(1/4))*(H1['Tgc']-H1['Tdbc']))**(1/4))-273
H1.head()
#Haven 2
H2['Tmrc']=((((H2['Tgc']+273)**4)+((0.25*(10**8))/0.95)*(((abs(H2['Tgc']-H2['Tdbc']))/0.051)**(1/4))*(H2['Tgc']-H2['Tdbc']))**(1/4))-273
H2.head()
#Haven 4
H4['Tmrc']=((((H4['Tgc']+273)**4)+((0.25*(10**8))/0.95)*(((abs(H4['Tgc']-H4['Tdbc']))/0.038)**(1/4))*(H4['Tgc']-H4['Tdbc']))**(1/4))-273
H4.head()
# Haven 5
H5['Tmrc']=((((H5['Tgc']+273)**4)+((0.25*(10**8))/0.95)*(((abs(H5['Tgc']-H5['Tdbc']))/0.051)**(1/4))*(H5['Tgc']-H5['Tdbc']))**(1/4))-273
H5.head()
#HL1
HL1['Tmrc']=((((HL1['Tgc']+273)**4)+((0.25*(10**8))/0.95)*(((abs(HL1['Tgc']-HL1['Tdbc']))/0.051)**(1/4))*(HL1['Tgc']-HL1['Tdbc']))**(1/4))-273
HL1.head()
#HL2
HL2['Tmrc']=((((HL2['Tgc']+273)**4)+((0.25*(10**8))/0.95)*(((abs(HL2['Tgc']-HL2['Tdbc']))/0.051)**(1/4))*(HL2['Tgc']-HL2['Tdbc']))**(1/4))-273
HL2.head()
#HL3
HL3['Tmrc']=((((HL3['Tgc']+273)**4)+((0.25*(10**8))/0.95)*(((abs(HL3['Tgc']-HL3['Tdbc']))/0.051)**(1/4))*(HL3['Tgc']-HL3['Tdbc']))**(1/4))-273
HL3.head()


# In[15]:


#Room Average calcs for temeprature and RH
RM3['Tdbcav']= (RM3['Tdbc1']+RM3['Tdbc2'])/2
RM3['TRHav']= (RM3['RH1']+RM3['RH2'])/2
RM3.head()


# In[17]:


# Perform stats on the Sensor Pod data, Output stats to csv file
#Haven1
print(H1.describe())
H1st= H1.describe()
H1st.to_csv('H1st.csv')
#Haven 2
H2st= H2.describe()
H2st.to_csv('H2st.csv')
#Haven 3
H3st = H3.describe()
H3st.to_csv('H3st.csv')
#Haven 6
H6st = H6.describe()
H6st.to_csv('H6st.csv')
#Haven 4
H4st= H4.describe()
H4st.to_csv('H4st.csv')
#Haven 5
H5st= H5.describe()
H5st.to_csv('H5st.csv')
#HL1
HL1st= HL1.describe()
HL1st.to_csv('HL1st.csv')
#HL2
HL2st= HL2.describe()
HL2st.to_csv('HL2st.csv')
#HL3
HL3st= HL3.describe()
HL3st.to_csv('HL3st.csv')
#Room stats
RM3st=RM3.describe()
RM3st.to_csv('RM3st.csv')


# In[18]:


# Output the Processed data to a .csv file
#Haven 1
H1.to_csv('H1Pod_processed.csv',index=True)
#Haven 2
H2.to_csv('H2Pod_processed.csv',index=True)
#Haven 3
H3.to_csv('H3Pod_processed.csv',index=True)
#Haven 6
H6.to_csv('H6Pod_processed.csv',index=True)
#Haven 4
H4.to_csv('H4Pod_processed.csv',index=True)
#haven 5
H5.to_csv('H5Pod_processed.csv',index=True)
#HL1
HL1.to_csv('HL1Pod_processed.csv',index=True)
#HL2
HL2.to_csv('HL2Pod_processed.csv',index=True)
#HL3
HL3.to_csv('HL3Pod_processed.csv',index=True)
#RM3
RM3.to_csv('RM3_processed.csv',index=True)


# In[26]:


#Make a line plot of Tdb, Tmr
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(H1['Tdbc'], color ='blue', label='Tdbc')
plt.plot(H1['Tmrc'], color ='red', label='Tmrc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Haven 1Temp Profile')
#show.fig()
plt.savefig('Haven 1 Temp Profile.png')


# In[27]:


# Make a plot of RH for qulaity checks
plt.plot(H1['RH%'], color ='blue', label='RH')
plt.legend()
plt.xlabel('Date')
plt.ylabel('RElative Humidity, %')
plt.title('Haven 1 RH Profile')
#show.fig()
plt.savefig('Haven 1 RH Profile.png')


# In[19]:


fig = plt.figure()
plt.plot(H2['Tdbc'], color ='blue', label='Tdbc')
plt.plot(H2['Tmrc'], color ='red', label='Tmrc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Haven 2Temp Profile')
#show.fig()
plt.savefig('Haven 2 Temp Profile.png')


# In[20]:


# Make a plot of RH for qulaity checks
plt.plot(H2['RH%'], color ='blue', label='RH')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Relative Humidity, %')
plt.title('Haven 2 RH Profile')
#show.fig()
plt.savefig('Haven 2 RH Profile.png')


# In[21]:


#Haven 3 temp plot
fig = plt.figure()
plt.plot(H3['Tdbc'], color ='blue', label='Tdbc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Haven 3 Temp Profile')
#show.fig()
plt.savefig('Haven 3 Temp Profile.png')


# In[22]:


#Haven 6 temp plot
fig = plt.figure()
plt.plot(H6['Tdbc'], color ='blue', label='Tdbc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Haven 6 Temp Profile')
#show.fig()
plt.savefig('Haven 6 Temp Profile.png')


# In[23]:


fig = plt.figure()
plt.plot(H4['Tdbc'], color ='blue', label='Tdbc')
plt.plot(H4['Tmrc'], color ='red', label='Tmrc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Haven 4 Temp Profile')
#show.fig()
plt.savefig('Haven 4 Temp Profile.png')


# In[24]:


# Make a plot of RH for qulaity checks
plt.plot(H4['RH%'], color ='blue', label='RH')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Relative Humidity, %')
plt.title('Haven 4 RH Profile')
#show.fig()
plt.savefig('Haven 4 RH Profile.png')


# In[25]:


fig = plt.figure()
plt.plot(H5['Tdbc'], color ='blue', label='Tdbc')
plt.plot(H5['Tmrc'], color ='red', label='Tmrc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Haven 5 Temp Profile')
#show.fig()
plt.savefig('Haven 5 Temp Profile.png')


# In[26]:


# Make a plot of RH for qulaity checks
plt.plot(H5['RH%'], color ='blue', label='RH')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Relative Humidity, %')
plt.title('Haven 5 RH Profile')
#show.fig()
plt.savefig('Haven 5 RH Profile.png')


# In[27]:


fig = plt.figure()
plt.plot(HL1['Tdbc'], color ='blue', label='Tdbc')
plt.plot(HL1['Tmrc'], color ='red', label='Tmrc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Heat Lamp 1 Temp Profile')
#show.fig()
plt.savefig('Heat Lamp 1 Temp Profile.png')


# In[29]:


#HL1 Do not run for January Turn
# Make a plot of RH for qulaity checks
#plt.plot(HL1['RH'], color ='blue', label='RH')
#plt.legend()
#plt.xlabel('Date')
#plt.ylabel('Relative Humidity, %')
#plt.title('Heat Lamp 1 RH Profile')
#show.fig()
#plt.savefig('Heat Lamp 1 RH Profile.png')


# In[30]:


fig = plt.figure()
plt.plot(HL2['Tdbc'], color ='blue', label='Tdbc')
plt.plot(HL2['Tmrc'], color ='red', label='Tmrc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Heat Lamp 2 Temp Profile')
#show.fig()
plt.savefig('Heat Lamp 2 Temp Profile.png')


# In[31]:



# Make a plot of RH for qulaity checks
plt.plot(HL2['RH%'], color ='blue', label='RH')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Relative Humidity, %')
plt.title('Heat Lamp 2 RH Profile')
#show.fig()
plt.savefig('Heat Lamp 2 RH Profile.png')


# In[32]:


fig = plt.figure()
plt.plot(HL3['Tdbc'], color ='blue', label='Tdbc')
plt.plot(HL3['Tmrc'], color ='red', label='Tmrc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Heat Lamp 3 Temp Profile')
#show.fig()
plt.savefig('Heat Lamp 3 Temp Profile.png')


# In[33]:


#Room temp
fig = plt.figure()
plt.plot(RM3['Tdbc1'], color ='blue', label='Tdbc')
plt.plot(RM3['Tdbc2'], color ='red', label='Tmrc')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temeprature, C')
plt.title('Room 3 Temp Profile')
#show.fig()
plt.savefig('Room 3 Temp Profile.png')


# In[35]:


fig = plt.figure()
plt.plot(RM3['RH1'], color ='blue', label='RH1')
plt.plot(RM3['RH2'], color ='red', label='RH2')
plt.legend()
plt.xlabel('Date')
plt.ylabel('RElative Humidity, %')
plt.title('Room 3 RH Profile')
#show.fig()
plt.savefig('Room 3 RH Profile.png')


# In[ ]:


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# In[ ]:


#Readi in the Stats files and rename the columns to include the unit in the column name
#Haven 1
series1 = pd.read_csv("H1st.csv")
series1.columns = ['stat','TdbfH1','TdbcH1','TgfH1','TgcH1','RH%H1','TmrcH1']
#Haven 2
series2 = pd.read_csv("H2st.csv")
series2.columns = ['stat','TdbfH2','TdbcH2','TgfH2','TgcH2','RH%H2','TmrcH2']
#Haven 3
series3 = pd.read_csv("H3st.csv")
series3.columns = ['stat','TdbfH3','TdbcH3']
#Haven 4
series4 = pd.read_csv("H4st.csv")
series4.columns = ['stat','TdbfH4','TdbcH4','TgfH4','TgcH4','RH%H4','TmrcH4']
#Haven 5
series5 = pd.read_csv("H5st.csv")
series5.columns = ['stat','TdbfH5','TdbcH5','TgfH5','TgcH5','RH%H5','TmrcH5']
#HAven 6
series6 = pd.read_csv("H6st.csv")
series6.columns = ['stat','TdbfH6','TdbcH6']
#HL 1 Add in RH for second Turn
series7 = pd.read_csv("HL1st.csv")
series7.columns = ['stat','TdbfHL1','TdbcHL1','TgfHL1','TgcHL1','TmrcHL1']
#HL2
series8 = pd.read_csv("HL2st.csv")
series8.columns = ['stat','TdbfHL2','TdbcHL2','TgfHL2','TgcHL2','RH%HL2','TmrcHL2']
#HL3
series9 = pd.read_csv("HL3st.csv")
series9.columns = ['stat','TdbfHL3','TdbcHL3','TgfHL3','TgcHL3','TmrcHL3']
#RM 3
series10 = pd.read_csv("RM3st.csv")
series10.columns = ['stat','TdbfRM31','TdbcRM31','TdbfRM32','TdbcRM32','RH1RM3', 'RH2RM3','TdbcavRM3','TRHavRM3']


# In[ ]:


#Merge DataFrames to form 1 df of all stats
RM3a = pd.merge(left=series1, right=series2, how='left', left_on='stat', right_on='stat')
RM3b = pd.merge(left=RM3a, right=series3, how='left', left_on='stat', right_on='stat')
RM3c = pd.merge(left=RM3b, right=series4, how='left', left_on='stat', right_on='stat')
RM3d = pd.merge(left=RM3c, right=series5, how='left', left_on='stat', right_on='stat')
RM3e = pd.merge(left=RM3d, right=series6, how='left', left_on='stat', right_on='stat')
RM3f = pd.merge(left=RM3e, right=series7, how='left', left_on='stat', right_on='stat')
RM3g = pd.merge(left=RM3f, right=series8, how='left', left_on='stat', right_on='stat')
RM3h = pd.merge(left=RM3g, right=series9, how='left', left_on='stat', right_on='stat')
RM3 = pd.merge(left=RM3h, right=series10, how='left', left_on='stat', right_on='stat')
RM3.head()


# In[ ]:


#output all stats data frame to csv
RM3.to_csv('RM3totst_processed.csv',index=True)

