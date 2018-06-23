# Code ranks countries based on scientic output, GDP, and Renewable energy per capita
"""
Created on Sat Jun 23 09:24:03 2018

@author: btayo
"""

import pandas as pd
import numpy as np

#RENEWABLE ENEGY DATA
df = pd.read_excel("Energy Indicators.xls")
df.replace('...',np.nan,inplace=True)

energy1=(df.drop(['Unnamed: 0','Unnamed: 1'],axis=1)
.drop(range(0,16))   
.rename(columns={'Environmental Indicators: Energy':'Country', 'Unnamed: 3':'Energy Supply', 
                 'Unnamed: 4':'Energy Supply per Capita', 'Unnamed: 5':'% Renewable'}))

energy=energy1.drop(range(243,281))
energy['Country']=energy['Country'].str.split('\d+').str[0]
energy['Country']=energy['Country'].str.split('(').str[0]

energy['Country'].replace(["Republic of Korea","United States of America",
                           "United Kingdom of Great Britain and Northern Ireland",
                           "China, Hong Kong Special Administrative Region"],["South Korea","United States",
                                                                              "United Kingdom","Hong Kong"],inplace=True)
energy['Energy Supply'] = 1000000.0*energy['Energy Supply']

country_new=[]
for i in range(16,243):
    if energy['Country'][i][-1]==' ':
        country_new = np.append(country_new,energy['Country'][i][:-1])
    else:
        country_new=np.append(country_new, energy['Country'][i])  
        
energy['Country']=country_new

#GDP DATA
Df=pd.read_csv('world_bank.csv')
Df.replace('...',np.nan,inplace=True)        

Df3=Df.drop(['Unnamed: 2','Unnamed: 3'],axis=1)
GDP=Df3.drop(range(4))

col_names=['Country', 'Code']
for i in range(1960,2016):
    col_names=np.append(col_names,str(i))
    
GDP.columns=col_names

GDP['Country']=GDP['Country'].replace(["Korea, Rep.","Iran, Islamic Rep.","Hong Kong SAR, China"],
                                      ["South Korea","Iran","Hong Kong"])

#ScimEn DATASET

ScimEn=pd.read_excel('scimagojr-3.xlsx')

#Combine three datasets

energy.set_index('Country',inplace=True)
GDP.set_index('Country',inplace=True)
ScimEn.set_index('Country',inplace=True)


total_df1=pd.merge(ScimEn, energy, how='inner', left_index=True, right_index=True) 
total = pd.merge(total_df1,GDP, how='inner', left_index=True, right_index=True)

final_df=total[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 
 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007',
 '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']][0:15]

print(final_df)    