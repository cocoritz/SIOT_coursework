# SIOT_coursework

As electricity production generates an important amount of greenhouse gas emissions, rethinking our electricity consumption behaviour is crucial to address climate change issues. 

This porject explored the correlation between a student house energy consumption and the amount of shared information about climate change on Twitter. In other words: **Does  alarming ‘energy and climate change’ news impact my household energy consumption behaviour?** 

View the project web interface:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/cocoritz/siot_coursework/main/streamlit_app.py)

## Coursework 1: Sensing and data collection 

The data collection directory contains all scripts related to the collection of two data streams: a student household energy consumption and the amount of news about climate change on Twitter.

**Files description:**

-`lightsensors_to_MongoDB.ino` : Script for programing an esp32 which collect flashing light on my electricity meters ( 1 flashes = 1 Wh)
-`correlation_twitter_energy_analysis` : Script for calling and collecting the tweets related to climate change and energy

Csv files containing the data as a backup for Mongodb are all stored in data storage folder:
-`readings` : data of the original energy readings
-`tweets` : data of the original tweets readings
-`readings_clean` : clean energy data with noanomalies)-resampled in hours
-`tweets_clean` : clean tweets data with no anomalies)-resampled in hours
-`energy_prediction`: values of the enrgy predictions in the next days

#### It is important to note that the script files will not run without the API keys and credentials files. These have not been committed to GitHub.

## Coursework 2: Internet of Things and interface

The data analysis contains all script related to cleaning, correlation, prediction and visualisation of the data collection.

**Files description:**

-`Twitter_data_analysis.py`: Script cleaning and analysising the twitter data
-`Energy_data_analysis_&_prediction.py`: Script cleaning, analysing and predicting the energy consumption data
-`correlation_twitter_energy_analysis.py`: Script exploring the correlation between the two data streams 
-`SMS.py`: script to send the sms based on prediction compare to actual values

-`streamlit_app.py`: Script to run the streamlit app 
-requirments.txt : specifying what python packages are required to run `streamlit_app.py`

#### the project was powered by aws, MongoDB Atlas and streamlit
