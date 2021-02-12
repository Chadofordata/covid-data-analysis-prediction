import requests
from datetime import timedelta, date
import pandas as pd

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

##day='2021-01-30'
df_subregions=pd.DataFrame()
df_regions=pd.DataFrame()

start_date=date.today() - timedelta(days=7)
end_date = date.today()
for single_date in daterange(start_date, end_date):
    day = single_date.strftime("%Y-%m-%d")
    api_url = f'https://api.covid19tracking.narrativa.com/api/{day}/country/spain'
    data_daily = requests.get(api_url).json()['dates'][day]['countries']['Spain']['regions']
    for region in data_daily:
        df_regions=df_regions.append(region,ignore_index=True)
       # if region['name_es'] =='Barcelona': # in case you want to filter the subregion
        for sub_region in region['sub_regions']:
              df_subregions=df_subregions.append(sub_region,ignore_index=True)

print(df_subregions[['date','id','today_confirmed','today_new_confirmed','today_vs_yesterday_confirmed','yesterday_confirmed']].to_string())
# to see what is writing into csv
df_subregions.to_csv(path_or_buf='data_export_90days.csv', index=False) #creating csv file



