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
df_tweets = df_tweets['number_of_tweets'].resample('H').sum()
#st.write(df_tweets)
#df_tweets.plot()

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

#Resample 
df_energy = df_energy['Watts-hour'].resample('H').sum()
st.write(df_energy)

df = pd.merge(df_energy, df_tweets,on='create_at',how='right')

st.write(df)


# def main():
#     page = st.sidebar.selectbox(
#         "Select a Page",
#         [
#             "Original data",
#             "Analysed data",
#             "Have a look"
            
#         ]
#     )

#     #First Page
#     if page == "Original data":
#         homepage()

#     #Second Page
#     elif page == "Analysed data":
#         analyseddata()
    
#     #Third Page
#     elif page == "Have a look":
#         information()

  

# def homepage():
#     st.write("""
#         # Sensing and Iot
#         ### original data ###
#         #""")
#     #tickers = ('#climatechange', '#energy','#energycrisis')
#     #dropdown= st.multiselect('Pick your #',tickers)

#     #start= st.date_input('Start',value= pd.to_datetime('2021-12-01'))
#     #end= st.date_input('End',value= pd.to_datetime('2021-12-20'))

#     image1='<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=d315592c-260e-40a6-b67f-bb67e628d83d&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>'
#     chart1= st.components.v1.html(image1, width=640, height=480, scrolling=False)

#     image2='<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=d24155ad-c4b4-4489-bbf7-efc169eb7a76&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>'
#     chart2= st.components.v1.html(image2, width=640, height=480, scrolling=False)

       
# def analyseddata():
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

 
        
# def information():
#     class Tweet(object):
#         def __init__(self, s, embed_str=False):
#             if not embed_str:
#                 # Use Twitter's oEmbed API
#                 # https://dev.twitter.com/web/embedded-tweets
#                 api = "https://publish.twitter.com/oembed?url={}".format(s)
#                 response = requests.get(api)
#                 self.text = response.json()["html"]
#             else:
#                 self.text = s

#         def _repr_html_(self):
#             return self.text

#         def component(self):
#             return components.html(self.text, height=600)


#     t = Tweet("https://twitter.com/OReillyMedia/status/901048172738482176").component()


# if __name__ == "__main__":
#     main()
