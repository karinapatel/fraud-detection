import pandas as pd

#converts certain columns to date time using pandas
def todatetime(df,columns=('event_created', 'event_end', 'event_published', 'event_start')):
    for c in columns:
        df[c]=pd.to_datetime(df[c],unit='s')