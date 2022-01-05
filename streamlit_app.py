# streamlit_app.py
import streamlit as st
import pymongo
import pandas as pd
import pymongo
from pymongo import MongoClient
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import requests
import streamlit.components.v1 as components
import numpy as np
from datetime import datetime, timezone
import statsmodels 
from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.tools

def main():
    page = st.sidebar.selectbox("Select a Page",["View original data", "View clean and analysed data","Want to know more?"])

    #First Page
    if page == "View original data":
        homepage()

    #Second Page
    elif page == "View clean and analysed data":
        analyseddata()
    
    #Third Page
    elif page == "Want to know more?":
        information()
        
def homepage():
    
    st.title('Sensing and Iot')
    st.write('This projects aims to explore the correlation between the amount of energy a student house uses and the amount of tweets about the impact of energy on climate change.')
    
    st.subheader('Original data')
    
    st.markdown('First data stream') 
    st.text('Student household energy consumption')
    image1='<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=d315592c-260e-40a6-b67f-bb67e628d83d&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>'
    chart1= st.components.v1.html(image1, width=640, height=480, scrolling=False)
    st.text("")
    st.text("")
    st.text("")
    st.markdown('Second data stream')
    st.text('Amount of tweets containing climate change and energy words')             
    image2='<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=d24155ad-c4b4-4489-bbf7-efc169eb7a76&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>'
    chart2= st.components.v1.html(image2, width=640, height=480, scrolling=False)

def analyseddata():
#     client_URI = "mongodb+srv://Coline:LfCG6401@cluster0.82bjh.mongodb.net/Twitter_API?retryWrites=true&w=majority"
#     #Load database
#     myclient = MongoClient(client_URI)
#     mydb = myclient.Twitter 
#     mycol = mydb.energy_and_climate_tweets

#     #Extract data and keep relevant columns
#     extracted_data = mycol.find({},{"create_at":1 ,"_id":1})
#     x_tweets = list(extracted_data)
#     df_tweets= pd.DataFrame(x_tweets)
#     df.plt()

    st.title('Analysed data')
    st.write('After being collected, data were cleaned and analysed')
    
    st.subheader(' Student household energy consumption over time')
    DATA_URL = ('Energy_consumption.csv')
    df_energy = pd.read_csv(DATA_URL)

    #Put same date format as tweets data 
    df_energy['ts']=pd.to_datetime(df_energy['ts'])
    df_energy.drop('sensors', axis = 1, inplace= True)
    df_energy= df_energy.rename(columns={'ts': 'create_at'})
    df_energy= df_energy.rename(columns={'newlight': 'Watts-hour'})

    #Keep relevant time
    filt = ((df_energy['create_at'] <= pd.to_datetime('2021-12-19 00:00'))& (df_energy['create_at'] >= pd.to_datetime('2021-12-05 17:00')))
    df_energy=df_energy.loc[filt]

    #Set time as index
    df_energy.set_index('create_at', inplace=True)
    df_energy.index=pd.to_datetime(df_energy.index)
    

  
    DATA_URL = ('Tweets_climatechange_and_energy.csv')
    df_tweets = pd.read_csv(DATA_URL)

    def remove_timezone(dt):
        return dt.replace(tzinfo=None)

    df_tweets['create_at']=pd.to_datetime(df_tweets['create_at'])
    df_tweets['create_at'] = df_tweets['create_at'].apply(remove_timezone)

    # Keep relevant time
    filt = ((df_tweets['create_at'] <= pd.to_datetime('2021-12-19 00:00'))& (df_tweets['create_at'] >= pd.to_datetime('2021-12-05 17:00')))
    df_tweets=df_tweets.loc[filt]

    # set time as index
    df_tweets.set_index('create_at', inplace=True)

    #Simplify calculation
    df_tweets['number_of_tweets'] = 1
    df_tweets.drop('_id',axis= 1, inplace= True)
    df_tweets.drop('text',axis= 1, inplace= True)

    # Resample per hour
    
    option = st.selectbox('Choose your sampling rate',('Minute','Hour', 'Day', 'Week','Month'))
    if option == 'Minute':
        df_tweets1 = df_tweets['number_of_tweets'].resample('T').sum()
        df_energy1 = df_energy['Watts-hour'].resample('T').sum()
    if option == 'Hour':
        df_tweets1 = df_tweets['number_of_tweets'].resample('H').sum()
        df_energy1 = df_energy['Watts-hour'].resample('H').sum()
    if option == 'Day':
        df_tweets1 = df_tweets['number_of_tweets'].resample('D').sum()
        df_energy1 = df_energy['Watts-hour'].resample('D').sum()
    if option == 'Week':
        df_tweets1 = df_tweets['number_of_tweets'].resample('W').sum()
        df_energy1 = df_energy['Watts-hour'].resample('W').sum()
    if option == 'Month':
        df_tweets1 = df_tweets['number_of_tweets'].resample('M').sum()
        df_energy1 = df_energy['Watts-hour'].resample('M').sum()
    
    st.caption('Click and play with the charts to zoom in')
    st.line_chart(df_energy1)
    st.subheader(' Amount of tweets over time')
    st.caption('Click and play with the charts to zoom in')   
    st.line_chart(df_tweets1)
    

    df_tweets = df_tweets['number_of_tweets'].resample('H').sum()
    df_energy = df_energy['Watts-hour'].resample('H').sum()
    df = pd.merge(df_energy, df_tweets,on='create_at',how='right')
    #st.line_chart(df)
    
    st.subheader(' Normalised data')
    st.text('This aims to easily visualise potentiel correlation')
    st.caption('Click and play with the charts to zoom in')
    ndata = df.copy(deep=True)
    stats = {}
    mean = np.mean(ndata)
    stdv = np.std(ndata)
    stats = {"mean":mean,"stdv":stdv}
    ndata = (ndata - mean) / stdv
    st.line_chart(ndata)
    
    
    st.header('Correlation')
    st.caption('This shows the seasonality and trend of the data streams')
    
    trend_series = []
    for i, name in enumerate(df.columns.values):
        decomposed = seasonal_decompose(df[name])
        trend_series.append(decomposed.trend)
        figure = decomposed.plot()
        st.plotly_chart(figure)
        figure.axes[0].set_title(name)
        trends = pd.concat(trend_series, axis=1)
    
    st.subheader('This shows the correlation of the data streams')
    t = df['Watts-hour']
    o = df['number_of_tweets']
    
    fig = plt.figure(figsize=(7, 2))
    plt.scatter(t, o)
   
    st.pyplot(fig)
    
    t = df['Watts-hour']
    o = df['number_of_tweets']
    
    fig = plt.figure(figsize=(7, 2))
    plt.scatter(o, t)
    
    st.pyplot(fig)
   
    
     
def information():
    st.Title('More information about climate change and energy')
    st.header('This is intresting posts i came across during my project!')
    class Tweet(object):
        def __init__(self, s, embed_str=False):
            if not embed_str:
                # Use Twitter's oEmbed API
                # https://dev.twitter.com/web/embedded-tweets
                api = "https://publish.twitter.com/oembed?url={}".format(s)
                response = requests.get(api)
                self.text = response.json()["html"]
            else:
                self.text = s

        def _repr_html_(self):
            return self.text

        def component(self):
            return components.html(self.text, height=600)


    t = Tweet("https://twitter.com/GasPriceWizard/status/1478400020672094213").component()
   

if __name__ == "__main__":
    main()
    
    
    
    
