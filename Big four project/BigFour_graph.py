
# # Big four project
# 
'''
This graph presents the variations of the ranking of the Top four teams (Manchester United, Liverpool FC, Arsenal FC and Chelsea FC)
in England at the end of each season since the creation of the premier league as a replacement of Division 1 at the start of 1992/193 season.
Data was scrapped from four wikipedia pages that included tables of all results of these teams since the start of organised football leagues
in England.
https://en.wikipedia.org/wiki/List_of_Chelsea_F.C._seasons
https://en.wikipedia.org/wiki/List_of_Liverpool_F.C._seasons
https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._seasons
https://en.wikipedia.org/wiki/List_of_Arsenal_F.C._seasons

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


arsenalxls = pd.ExcelFile("arsenal.xlsx") 
arsenal = pd.read_excel(arsenalxls,  usecols = [0,1,9],skiprows=100)
arsenal.columns =['Season', 'Division', 'Position']
arsenal['Position'] = arsenal['Position'].map(lambda x: x.lstrip('+-').rstrip('thndrdst'))
arsenal['Season'] = arsenal['Season'].str.split('–').str[0].apply(pd.to_numeric, errors='coerce')+1

liverpoolxls = pd.ExcelFile("liverpool.xlsx") 
liverpool = pd.read_excel(liverpoolxls,  usecols = [0,1,9],skiprows=93)
liverpool.columns =['Season', 'Division', 'Position']
liverpool['Position'] = liverpool['Position'].map(lambda x: x.lstrip('+-').rstrip('thndrdst'))
liverpool['Season'] = liverpool['Season'].str.split('–').str[0].apply(pd.to_numeric, errors='coerce')+1
    
muxls = pd.ExcelFile("mu.xlsx") 
mu = pd.read_excel(muxls,  usecols = [0,1,9],skiprows=99)
mu.columns =['Season', 'Division', 'Position']
mu['Position'] = mu['Position'].map(lambda x: x.lstrip('+-').rstrip('thndrdst'))
mu['Season'] = mu['Season'].str.split('–').str[0].apply(pd.to_numeric, errors='coerce')+1
    
    
chelseaxls = pd.ExcelFile("chelsea.xlsx") 
chelsea = pd.read_excel(chelseaxls,  usecols = [0,1,9],skiprows=80, skipfooter=2)
chelsea.columns =['Season', 'Division', 'Position']
chelsea['Position'] = chelsea['Position'].map(lambda x: x.lstrip('+-').rstrip('thndrdst'))
chelsea['Season'] = chelsea['Season'].str.split('–').str[0].apply(pd.to_numeric, errors='coerce')+1



plt.figure(figsize=(16, 8))

plt.plot(arsenal['Season'].values,arsenal['Position'].values, '#650021', label = 'Arsenal')
plt.plot(arsenal['Season'].values,mu['Position'].values, 'r', label = 'Manchester United')
plt.plot(arsenal['Season'].values,chelsea['Position'].values, '#0504aa', label = 'Chelsea')
plt.plot(arsenal['Season'].values,liverpool['Position'].values, '#02ab2e', label = 'Liverpool')
         
plt.gca().axis([1993, 2018, 15, 0])

#arsenal['Season']

plt.xticks(arsenal['Season'].values, rotation = '45')

plt.xlabel('Seasons')
plt.ylabel('Position')
plt.title('Position of Top4 clubs since start of Premier league in England')
plt.legend(loc = 'lower right', frameon = False)


plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
