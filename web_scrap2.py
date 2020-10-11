import pandas as pd 
import numpy as np 
import datetime 

hldy_years = ['2020','2021','2022']

hldy_names = ['New Years Day', 'Martin Luther King, Jr. Day', "Washington's Birthday", 'Good Friday', 'Memorial Day', 'Independence Day', 'Labor Day', 'Thanksgiving Day', 'Christmas Day']

hldy_days = ['Wednesday, January 1', 'Friday, January 1', ' — ', 'Monday, January 20', 'Monday, January 18', 'Monday, January 17', 'Monday, February 17', 'Monday, February 15', 'Monday, February 21', 'Friday, April 10', 'Friday, April 2', 'Friday, April 15', 'Monday, May 25', 'Monday, May 31', 'Monday, May 30', 'Friday, July 3 (July 4 holiday observed)', 'Monday, July 5 (July 4 holiday observed)', 'Monday, July 4', 'Monday, September 7', 'Monday, September 6', 'Monday, September 5', 'Thursday, November 26*', 'Thursday, November 25*', 'Thursday, November 24*', 'Friday, December 25**', 'Friday, December 24 (Christmas holiday observed)', 'Monday, December 26 (Christmas holiday observed)']

cols = len(hldy_years)
print(cols)
print()

rows = len(hldy_names)
print(rows)
print()

z = len(hldy_days)
print(z)
print()
i = int(len(hldy_days)/len(hldy_years))
print(i)

hldy_years = hldy_years * i
print(hldy_years)

hldy_years_df = pd.DataFrame()
hldy_years_df['yr'] = hldy_years

hldy_days_df = pd.DataFrame()
hldy_days_df['days'] = hldy_days
hldy_days_df['days'] = hldy_days_df['days'].str.split(",",expand=True)[1]
hldy_days_df['days'] = hldy_days_df['days'].str.strip('*')
#hldy_days_df['mnth_day'] = hldy_days_df['days'].str.split(expand=True)[0] + hldy_days_df['days'].str.split(expand=True)[1].str.zfill(2)
hldy_days_df['mnth'] = hldy_days_df['days'].str.split(expand=True)[0]
hldy_days_df['day'] = hldy_days_df['days'].str.split(expand=True)[1].str.zfill(2)

hldy_days_df = hldy_days_df.join(hldy_years_df)
#hldy_days_df['dtx'] = hldy_days_df['mnth_day'] + hldy_days_df['yr']
#hldy_days_df = hldy_days_df.sort_values(['dtx'])

#hldy_days_df = hldy_days_df[['dtx']]
hldy_days_df = hldy_days_df[['mnth','day','yr']]
hldy_days_df['dtx'] = pd.to_datetime(hldy_days_df['mnth'] + hldy_days_df['day'].astype(str) + hldy_days_df['yr'].astype(str),format='%B%d%Y')
hldy_days_df = hldy_days_df[pd.notnull(hldy_days_df['dtx'])]
hldy_days_df = hldy_days_df[['dtx']].sort_values(['dtx'])
hldy_days_df = hldy_days_df['dtx'].dt.strftime('%m-%d-%Y')

# hldy_days_df.reset_index('dtx',drop=True,inplace=True)

# print(hldy_days_df.index.name)

print()
print()
print(hldy_days_df)

hldy_days_df.to_json (r'/home/masthan/DevOps/Python/NYSE_Holidays.json',orient='split',index=False)
