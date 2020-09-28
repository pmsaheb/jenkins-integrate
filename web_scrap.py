import requests
from bs4 import BeautifulSoup as Soup 
import pandas as pd 
import datetime 

#Read the NYSE market holiday calendars
source = requests.get('https://www.nyse.com/markets/hours-calendars').text 
soup = Soup(source,'html5lib')

# Create empty lists to store the holiday names, years and dates
hldy_years = []
hldy_names = []
hldy_days = []

# Pull the market holiday calendar table header that has all the years for which NYSE has 
# published the holiday calendar
hldy_table_h = soup.find('table',{"table table-layout-fixed"}).thead.tr
print()
print()

# Read all the years and append them to the years list
for td in hldy_table_h.find_all('td'):
    hldy_years.append(td.text)

# Exclude "Holiday" value from the list
hldy_years = hldy_years[1:]
n_years=len(hldy_years)
print(n_years)
print(hldy_years)

hldy_table_b = soup.find('table',{"table table-layout-fixed"}).tbody

for th in hldy_table_b.find_all('th'):
    hldy_names.append(th.text)

for td in hldy_table_b.find_all('td'):
    hldy_days.append(td.text)

print(hldy_names)
print()
print()

print(hldy_days)

#Convert the holiday schedule years, holiday schedule dates and days into Python DataFrames
hldy_years_df = pd.DataFrame() 
hldy_years_df['year'] = hldy_years 

hldy_names_df = pd.DataFrame()
hldy_names_df['holiday'] = hldy_names

i = int(len(hldy_days)/len(hldy_years))
hldy_years = hldy_years * i

hldy_days_df = pd.DataFrame()
hldy_days_df['days'] = hldy_days
hldy_days_df['days'] = hldy_days_df['days'].str.split(",",expand=True)[1]
hldy_days_df['days'] = hldy_days_df['days'].str.strip('*')
hldy_days_df['days'] = hldy_days_df['days'].str.split(expand=True)[0] + hldy_days_df['days'].str.split(expand=True)[1]

print(hldy_years_df)
print()
print()

hldy_years_df = hldy_years_df.transpose()
print(hldy_years_df)
print()
print()

print(hldy_names_df)
print()
print()

print(hldy_days_df)
