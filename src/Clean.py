#Clean data to categorize fraud or not fraud
def clean(df):
    fraudster =  ['fraudster_event' ,'fraudster','fraudster_att']
    df["Target"] = [a in fraudster for a in df['acct_type'] ]
    df["Target"] = df["Target"].astype(int)
    return df