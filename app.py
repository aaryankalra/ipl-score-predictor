import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = [
    'Mumbai Indians',
    'Chennai Super Kings',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Rajasthan Royals',
    'Kings XI Punjab',
    'Sunrisers Hyderabad',
    'Delhi Daredevils',
    'Delhi Capitals',
    'Deccan Chargers',
    'Punjab Kings',
    'Lucknow Super Giants',
    'Gujarat Titans',
    'Pune Warriors',
    'Gujarat Lions',
    'Royal Challengers Bengaluru',
    'Rising Pune Supergiant',
    'Kochi Tuskers Kerala',
    'Rising Pune Supergiants'
]

cities = ['Mumbai',
 'Kolkata',
 'Delhi',
 'Chennai',
 'Hyderabad',
 'Bangalore',
 'Chandigarh',
 'Jaipur',
 'Pune',
 'Dubai',
 'Abu Dhabi',
 'Ahmedabad',
 'Bengaluru',
 'Sharjah',
 'Visakhapatnam',
 'Durban',
 'Lucknow',
 'Dharamsala',
 'Centurion',
 'Rajkot',
 'Navi Mumbai',
 'Indore',
 'Johannesburg',
 'Port Elizabeth',
 'Cuttack',
 'Ranchi',
 'Cape Town',
 'Raipur',
 'Mohali',
'Kochi'
]

st.image('img1.png')

st.markdown("<h1 style='text-align: center;'>IPL Score Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict the total runs a team will score in an IPL innings with this ML model</p>", unsafe_allow_html=True)

st.write("###")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Choose Batting Team', sorted(teams)) 

with col2:
    bowling_team = st.selectbox('Choose Bowling Team', sorted(teams))
    
city = st.selectbox('Choose Venue', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score', min_value=0, max_value=250, step=1)
with col4:
    overs_done = st.number_input('Overs Done', min_value=5.0, max_value=20.0, step=0.1)
with col5:
    wickets_down = st.number_input('Wickets Down', min_value=0, max_value=10, step=1)
    
last_five = st.number_input('Runs in Last 5 Overs', min_value=0, max_value=60, step=1) 

if st.button('Predict Score'):
    balls_left = 120 - (overs_done)*6
    wickets_left = 10 - wickets_down
    crr = current_score/overs_done
    
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'current_score': [current_score],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'crr': [crr],
        'last_five': [last_five]
    })
    
    result = pipe.predict(input_df)
    final_score = str(int(result[0]))
    st.header('Predicted Final Score: ' + final_score)
