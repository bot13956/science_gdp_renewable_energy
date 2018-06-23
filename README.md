# science_gdp_renewable_energy

This code ranks countries by science output and correlates that to GDA and total energy supply per capita.

Energy Indicators.xls: is a list of indicators of energy supply and renewable electricity production from 
the United Nations for the year 2013.

world_bank.csv: csv file containing countries' GDP from 1960 to 2015 from World Bank.

scimagojr-3.xlsx: Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology which ranks 
countries based on their journal contributions in the aforementioned area. 

analysis.py: python code to import all three data sets, clean the data, perform analysis, 
and combine them based on following features:  ['Rank', 'Documents', 'Citable documents', 'Citations', 
'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', 
'% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
