import streamlit as st
import streamlit.components.v1 as components
import pymongo
from pymongo import MongoClient

@st.cache(hash_funcs={MongoClient: id})
def get_client():
    client_UR = "mongodb+srv://Coline:LfCG6401@cluster0.82bjh.mongodb.net/Twitter_API?retryWrites=true&w=majority"
    return MongoClient(client_UR)

client = get_client()
db = client.Twitters
collection = db.tweets

st.write(collection.find()[0])

