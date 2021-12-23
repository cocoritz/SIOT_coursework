# streamlit_app.py

import streamlit as st
import pymongo
import './styles.css'

# Initialize connection.
#client = pymongo.MongoClient(**st.secrets["mongo"])

# Pull data from the collection.
# Uses st.cache to only rerun when the query changes or after 10 min.
#@st.cache(ttl=600)
#def get_data():
    #db = client.mydb
    #items = db.mycollection.find()
    #items = list(items)  # make hashable for st.cache
    #return items

#items = get_data()

# Print results.
#for item in items:
    #st.write(f"{item['name']} has a :{item['pet']}:")



document.getElementById('app').innerHTML = `

<iframe style="background: #FFFFFF;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-twitter_api_project-zwapd/embed/charts?id=d315592c-260e-40a6-b67f-bb67e628d83d&maxDataAge=3600&theme=light&autoRefresh=true"></iframe>
`
