from pandas_datareader import data
from bokeh.plotting import figure, show, output_file
import datetime

start=datetime.datetime(2020,1,1)
end=datetime.datetime(2020,4,1)
df=(data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end))

def inc(c,o):
    if(c>o):
        value= "increased"
    elif(c<o):
        value= "decreased"
    else:
        value= "equal"
    return value


# for i in range(len(df)):
#     df["Status"]=inc((df["Close"][i]),(df["Open"][i]))

df["Status"]=[inc(c,o) for c, o in zip(df.Close,df.Open)]
df["Middle"]=(df.Close+df.Open)/2
df["Height"]=abs(df.Close-df.Open)

#Every layer is added to the graph in order that they are code(First the shadows appear,then the body is added)
p=figure(x_axis_type="datetime", width=1000, height=300, title="CandleStick")

p.grid.grid_line_alpha=0.3
#For shadows
p.segment(df.index,df.High,df.index,df.Low,color="Black")
hours_12=12*60*60*1000

# price_inc=df.index[df.Close>df.Open]
# price_dec=df.index[df.Open>df.Close]

p.rect(df.index[df.Status=="increased"],df.Middle[df.Status=="increased"], hours_12, df.Height[df.Status=="increased"], 
       fill_color="green", line_color="black")

p.rect(df.index[df.Status=="decreased"],df.Middle[df.Status=="decreased"], hours_12, df.Height[df.Status=="decreased"], 
       fill_color="red", line_color="black")

output_file("CS.html")
show(p)
