import streamlit as st
import streamlit.components.v1 as components
import pymongo

# Initialize connection.
#client = pymongo.MongoClient(**st.secrets["mongo"])
client_UR = "mongodb+srv://Coline:LfCG6401@cluster0.82bjh.mongodb.net/Twitter_API?retryWrites=true&w=majority"
client = MongoClient(client_UR)
mydb = client.Twitter # use or create a database named demo
mycollection = mydb.tweets #use or create a collection named tweet_collection

# Pull data from the collection.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache
    return items

items = get_data()

