# SIOT_coursework

As electricity production generates an important amount of greenhouse gas emissions, rethinking our electricity consumption behaviour is crucial to address climate change issues. 

This porject explored the correlation between a student house energy consumption and the amount of shared information about climate change on Twitter. In other words: **Does  alarming ‘energy and climate change’ news impact my household energy consumption behaviour?** 

View the project web interface:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/cocoritz/siot_coursework/main/streamlit_app.py)

## Coursework 1: Sensing and data collection 

The data collection directory contains all scripts related to the collection of two data streams: a student household energy consumption and the amount of news about climate change on Twitter.

**Files description:**

`lightsensors_to_MongoDB.ino` : Script for programing an esp32 which collect flashing light on my electricity meters ( 1 flashes = 1 Wh)
`xxx` : Script for calling and collecting the tweets related to climate change and energy 
`xxx` : script to set up AWS services to run continously xxx

`xxx and xxx` are csv files containing the data as a backup for Mongodb 

#### It is important to note that the script files will not run without the API keys and credentials files. These have not been committed to GitHub.

## Coursework 2: Internet of Things and interface

The data analysis contains all script related to cleaning, correlation, prediction and visualisation of the data collection.

**Files description:**

`xxx`: Script cleaning and analysising the twitter data
`xxx`: Script cleaning, analysing and predicting the energy consumption data
`xxx`: Script exploring the correlation between the two data streams 

`xxx`: Script to run the streamlit app 
requirments.txt : specifying what python packages are required to run xxx

#### the project was powered by aws, MongoDB Atlas and streamlit
