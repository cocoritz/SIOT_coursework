# streamlit_app.py

import streamlit as st
import pymongo
import pandas as pd
import pymongo
from pymongo import MongoClient
import streamlit.components.v1 as components
import matplotlib.pyplot as plt


def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Original data"
        ]
    )

    if page == "Original data":
        homepage()

def homepage():
    st.write("""
        # Sensing and Iot
        ### original data ###
        #""")
    #tickers = ('#climatechange', '#energy','#energycrisis')
    #dropdown= st.multiselect('Pick your #',tickers)

    #start= st.date_input('Start',value= pd.to_datetime('2021-12-01'))
    #end= st.date_input('End',value= pd.to_datetime('2021-12-20'))

    image1='<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=d315592c-260e-40a6-b67f-bb67e628d83d&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>'
    chart1= st.components.v1.html(image1, width=640, height=480, scrolling=False)

    image2='<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=d24155ad-c4b4-4489-bbf7-efc169eb7a76&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>'
    chart2= st.components.v1.html(image2, width=640, height=480, scrolling=False)

def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Analysed data"
        ]
    )

    if page == "Analysed data":
        analyseddata()
        
       
def analyseddata():
    
    client_URI = "mongodb+srv://Coline:LfCG6401@cluster0.82bjh.mongodb.net/Twitter_API?retryWrites=true&w=majority"
    #Load database
    myclient = MongoClient(client_URI)
    mydb = myclient.Twitter 
    mycol = mydb.energy_and_climate_tweets

    #Extract data and keep relevant columns
    extracted_data = mycol.find({},{"create_at":1 ,"_id":1})
    x_tweets = list(extracted_data)
    df_tweets= pd.DataFrame(x_tweets)
    print(df)

  
def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Intresting information"
        ]
    )

    if page == "Intresting information":
        information()
        
#def information():

if __name__ == "__main__":
    main()

#if len(dropdown)>0:
# df=pymongo.client.mydb
#  items = db.mycollection.find(dropdown,start,end)
#  items = list(items)  

#chart1 = alt.Chart(df).mark_line().encode().properties(width=500, height=300)
#chart2 = alt.Chart(df).mark_line().encode().properties(width=500, height=300)


                    


