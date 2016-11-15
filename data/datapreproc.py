import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

#Utah specific data for 1960 - 2012, cleaning
utah_data = pd.read_csv('CrimeStatebyUT.csv', skiprows = 5)[:-4] #skip footers werent working, manually ignored footer
utah_data = utah_data[['Year', 'Population', 'Violent crime total', 'Murder and nonnegligent Manslaughter', 'Forcible rape', 'Robbery', 'Aggravated assault', 'Property crime total', 'Burglary', 'Larceny-theft', 'Motor vehicle theft', 'Violent Crime rate', 'Murder and nonnegligent manslaughter rate', 'Forcible rape rate', 'Robbery rate', 'Aggravated assault rate', 'Property crime rate', 'Burglary rate', 'Larceny-theft rate', 'Motor vehicle theft rate']] #excluding last erroneous column

#Country specific data for 2012, cleanning
us_2012_data = pd.read_csv('CrimeOneYearofData2012.csv', skiprows = 6)[:-24] #skip footers werent working, manually ignored footer
us_2012_data = us_2012_data[['State', 'Population', 'Violent crime total', 'Murder and nonnegligent Manslaughter', 'Forcible rape', 'Robbery', 'Aggravated assault', 'Property crime total', 'Burglary', 'Larceny-theft', 'Larceny-theft', 'Motor vehicle theft', 'Violent Crime rate', 'Murder and nonnegligent manslaughter rate', 'Forcible rape rate', 'Robbery rate', 'Aggravated assault rate', 'Property crime rate', 'Burglary rate', 'Larceny-theft rate', 'Motor vehicle theft rate']] #excluding last erroneous column

#Coutry specific data for 1960 - 2012, 
us_all_data = pd.read_csv('CrimeStatebyState_all.csv', skiprows = 5)[:-6]
us_all_data = us_all_data[['Year', 'Population', 'Violent crime total', 'Murder and nonnegligent Manslaughter', 'Forcible rape', 'Robbery', 'Aggravated assault', 'Property crime total', 'Burglary', 'Larceny-theft', 'Motor vehicle theft', 'Violent Crime rate', 'Murder and nonnegligent manslaughter rate', 'Forcible rape rate', 'Robbery rate', 'Aggravated assault rate', 'Property crime rate', 'Burglary rate', 'Larceny-theft rate', 'Motor vehicle theft rate']]

#get column headers using: list(us_all_data.columns.values)
plt.title('Time series of Robbery rate across US')
plt.xlabel('Year')
plt.ylabel('Robbery rate (offenses per 100,000 people')
plt.plot(us_all_data['Year'], us_all_data['Robbery rate'])
plt.show()

#get column headers using: list(us_all_data.columns.values)
plt.title('Time series of Aggravated assault rate across US')
plt.xlabel('Year')
plt.ylabel('Aggravated assault rate (offenses per 100,000 people')
plt.plot(us_all_data['Year'], us_all_data['Aggravated assault rate'])
plt.show()

#get column headers using: list(us_all_data.columns.values)
plt.title('Time series of total violent crimes across US')
plt.xlabel('Year')
plt.ylabel('Total violent crimes')
plt.plot(us_all_data['Year'], us_all_data['Violent crime total'])
plt.show()

#list(utah_data.columns.values)
plt.title('Time series of Robbery rate in Utah')
plt.xlabel('Year')
plt.ylabel('Robbery rate (offenses per 100,000 people')
plt.plot(utah_data['Year'], utah_data['Robbery rate'])
plt.show()

#list(utah_data.columns.values)
plt.title('Time series of Aggravated assault rate in Utah')
plt.xlabel('Year')
plt.ylabel('Aggravated assault rate (offenses per 100,000 people')
plt.plot(utah_data['Year'], utah_data['Aggravated assault rate'])
plt.show()

#Utah counties specific data,cleaning
#TODO

#Poverty data
#TODO
#Example (todo, change parameters)
poverty_api = requests.get('http://api.census.gov/data/timeseries/poverty/histpov2?get=PCTPOV&time=2015&key=8afa7db9f8c03c019082aeb107ebbd1b34bb57d9')
pctpov = poverty_api.json()
print pctpov

#Education data
#TODO

#Employment data
#TODO

#Age




