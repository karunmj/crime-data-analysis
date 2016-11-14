import pandas as pd
import numpy as np
import requests

#Utah specific data, cleaning
utah_data = pd.read_csv('CrimeStatebyUT.csv', skiprows = 5)[:-4] #skip footers werent working, manually ignored footer
utah_data = utah_data[['Year', 'Population', 'Violent crime total', 'Murder and nonnegligent Manslaughter', 'Forcible rape', 'Robbery', 'Aggravated assault', 'Property crime total', 'Burglary', 'Larceny-theft', 'Motor vehicle theft', 'Violent Crime rate', 'Murder and nonnegligent manslaughter rate', 'Forcible rape rate', 'Robbery rate', 'Aggravated assault rate', 'Property crime rate', 'Burglary rate', 'Larceny-theft rate', 'Motor vehicle theft rate']] #excluding last erroneous column

#Country specific data, cleanning
us_2012_data = pd.read_csv('CrimeOneYearofData2012.csv', skiprows = 6)[:-24] #skip footers werent working, manually ignored footer
us_2012_data = us_2012_data[['State', 'Population', 'Violent crime total', 'Murder and nonnegligent Manslaughter', 'Forcible rape', 'Robbery', 'Aggravated assault', 'Property crime total', 'Burglary', 'Larceny-theft', 'Larceny-theft', 'Motor vehicle theft', 'Violent Crime rate', 'Murder and nonnegligent manslaughter rate', 'Forcible rape rate', 'Robbery rate', 'Aggravated assault rate', 'Property crime rate', 'Burglary rate', 'Larceny-theft rate', 'Motor vehicle theft rate']] #excluding last erroneous column

#Utah counties specific data,cleaning
#TODO

#Poverty data
#Example (todo, change parameters)
poverty_api = requests.get('http://api.census.gov/data/timeseries/poverty/histpov2?get=PCTPOV&time=2015&key=8afa7db9f8c03c019082aeb107ebbd1b34bb57d9')
pctpov = poverty_api.json()
print pctpov

#Education data
#TODO

#Employment data
#TODO

#Age utah_data




