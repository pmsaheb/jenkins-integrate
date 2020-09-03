import numpy as np
import pandas as pd

#url = ('https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv')
url = ('/home/masthan/Documents/Python/Trans.xlsx')
url2 = ('/home/masthan/Documents/Python/Trans2.xlsx')

#tips = pd.read_csv(url)
tips = pd.read_excel(url)
tips['total_cost'] = tips['Price'] * tips['total_items']
print(tips.head())
print()
print()

#tips = pd.DataFrame({'date1':[pd.Timestamp('2020-07-12')],
#'date2':[pd.Timestamp('2020-04-26')]})
tips['date1_year'] = tips['date1'].dt.year 
tips['date1_month'] = tips['date1'].dt.month 
tips['date3'] = tips['date1'] + pd.offsets.MonthBegin()
tips['date4'] = tips['date1'] - pd.offsets.MonthBegin()
tips['month_between'] = tips['date1'].dt.to_period('M') - tips['date2'].dt.to_period('M')
tips = tips[['trans_id','date1','date2','date3','date4','date1_year','date1_month']]
tips = tips.rename(columns={'month_between': 'months_between','date1_year':'_year'})
tips = tips.drop('date1_month',axis=1)
tips = tips.sort_values(['date1'])
print(tips.head())

sales = pd.read_excel(url)
print(sales.head())

