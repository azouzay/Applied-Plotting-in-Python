
## Graphic representation
# Project 1- Temperature Plot


#The data for this project comes from a subset of The National Centers for Environmental Information (NCEI)
#[Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily).
#The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# The following variables are provided:  
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 

# Objective is to write some a code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014.
# The area between the record high and record low temperatures for each day will be shaded.
# Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np

data=pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
data['Year']=data['Date'].apply(lambda x : x[:4])
data['Month-Day']=data['Date'].apply(lambda x : x[5:])
data=data[data['Month-Day']!='02-29'] # remove leap days
#data.head()


data_until2014=data[data['Date']<'2015-01-01']
#print(data_until2014['Date'].min(),data_until2014['Date'].max())

data_2015=data[data['Date']>='2015-01-01']
#print(data_2015['Date'].min(),data_2015['Date'].max())


record_high=data_until2014.groupby('Month-Day')['Data_Value'].max()
# record_high=record_high.reset_index()
# record_high=record_high.rename(index=str,columns={'Data_Value':'record_high'})
# #record_high.head()
# record_high.shape

record_low=data_until2014.groupby('Month-Day')['Data_Value'].min()

record_high_2015=data_2015.groupby('Month-Day')['Data_Value'].max()

record_low_2015=data_2015.groupby('Month-Day')['Data_Value'].min()
record_low_2015=record_low_2015.reset_index()
record_low_2015=record_low_2015.rename(index=str,columns={'Data_Value':'record_low_2015'})
#record_low.head()
#record_low_2015.shape


record_low_mge=record_low.reset_index()
record_low_2015_mge=record_low_2015.reset_index()
record_low_2015_mge=record_low_2015_mge.rename(index=str,columns={'Data_Value':'record_low_2015'})
data_low=pd.merge(record_low_mge,record_low_2015_mge,on='Month-Day')
data_low['min2015']=data_low['Data_Value']>data_low['record_low_2015']
index_low=np.where(data_low['min2015'])


record_high_mge=record_high.reset_index()
record_high_2015_mge=record_high_2015.reset_index()
record_high_2015_mge=record_high_2015_mge.rename(index=str,columns={'Data_Value':'record_high_2015'})
data_high=pd.merge(record_high_mge,record_high_2015_mge,on='Month-Day')
data_high['max2015']=data_high['record_high_2015']>data_high['Data_Value']
index_high=np.where(data_high['max2015'])


plt.figure()
# plot the linear data and the exponential data

plt.plot(record_high.values,'red',label='record high 2005-2014')
plt.plot(record_low.values,'blue',label='record low 2005-2014')
plt.xticks(range(0, len(record_high), 20), record_high.index[range(0, len(record_high), 20)], rotation = '45')

y_2015_high=data_high.iloc[index_high].record_high_2015
y_2015_low=data_low.iloc[index_low].record_low_2015
plt.scatter(index_high,y_2015_high,label='record high in 2015')
plt.scatter(index_low,y_2015_low,label='record low in 2015')


#plt.gca().fill_between(range(len(y1)), y2, y1, facecolor='grey', alpha=0.5)
plt.gca().axis([-5, 370, -750, 550])

plt.xlabel('Month-Day')
plt.ylabel('Temperatures')
plt.legend(loc=4)
plt.title('Temperatures in Ann Arbor, Michigan, US, 2005-2015')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
    
plt.show()

