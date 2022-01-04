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


# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])

# Pull data from the collection.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")

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




                    


