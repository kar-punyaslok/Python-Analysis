import pandas as pd
import pandas as pd

df=pd.read_csv("avocado.csv")
df["Date"]=pd.to_datetime(df["Date"])
albany_df=df.copy()[df["region"]=="Albany"]
albany_df.set_index("Date",inplace=True)
albany_df.sort_index(inplace=True)
albany_df['price25ma']=albany_df["AveragePrice"].rolling(25).mean()
albany_df["AveragePrice"].rolling(25).mean().plot()
albany_df.tail(3)


df=pd.read_csv("avocado.csv")
df["Date"]=pd.to_datetime(df["Date"])
df=df.copy()[df['type']=='organic']

df.sort_values('Date',ascending=True)

graph_df=pd.DataFrame()

for region in df['region'].unique()[:30]:
    print(region)
    region_df=df.copy()[df['region']==region]
    region_df.set_index('Date',inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f'{region}_price_ma20']=region_df['AveragePrice'].rolling(20).mean()
        
    if graph_df.empty:
        graph_df=region_df[[f'{region}_price_ma20']]
    else:
        graph_df=graph_df.join(region_df[f'{region}_price_ma20'])
        
        
graph_df.dropna().plot(legend=False)      