import streamlit as st
import numpy as np

def predict_win_probability(score, wickets, overs, target):
    # Dummy logic – replace with your model's prediction logic
    base_chance = (score / target) * (20 - overs) / 20
    pressure_factor = (10 - wickets) / 10
    probability = min(max(base_chance * pressure_factor * 100, 0), 100)
    return round(probability, 2)

st.set_page_config(page_title="Cricket Win Predictor", layout="wide")
st.title("🏏 Live Cricket Win Predictor")

score = st.number_input("Current Score", value=120)
wickets = st.slider("Wickets Lost", 0, 10, 4)
overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
target = st.number_input("Target Score", value=180)

if st.button("Predict Win Probability"):
    win_chance = predict_win_probability(score, wickets, overs, target)
    st.success(f"Win Probability: {win_chance} %")
    st.line_chart([30, 45, 55, win_chance])