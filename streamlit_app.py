# streamlit_app.py

import streamlit as st
import pymongo
import pandas as pd
import pymongo
import streamlit.components.v1 as components


st.set_page_config(page_title='Survey Results')
st.header('Sensing and IoT')
st.subheader('Energy')
tickers = ('#climatechange', '#energy','#energycrisis')
dropdown= st.multiselect('Pick your #',tickers)

start= st.date_input('Start',value= pd.to_datetime('2021-12-01'))
end= st.date_input('End',value= pd.to_datetime('2021-12-20'))

image='<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=d315592c-260e-40a6-b67f-bb67e628d83d&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>'
st.components.v1.html(image, width=640, height=480, scrolling=False)

st.subheader('Tweets')

image='<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=0ca4fa3b-3ff8-49cb-bd6e-1ae9c3a620cf&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>'
st.components.v1.html(image, width=640, height=480, scrolling=False)

#if len(dropdown)>0:
# df=pymongo.client.mydb
#  items = db.mycollection.find(dropdown,start,end)
#  items = list(items)  

                    


