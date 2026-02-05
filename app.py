import streamlit as st
import plotly.express as px
import time 
import random

@st.cache_data()
def load_data():
    time.sleep(1.5)
    df = px.data.iris()
    return df

with st.spinner():
    df = load_data()

col_x = st.select_slider("Choisis la colomne à plot"
                 ,options=["sepal_width", "sepal_length","petal_width", "petal_length",])
col_y = st.select_slider("Choisis la colomne à plot"
                 ,options=[ "sepal_length","sepal_width","petal_width", "petal_length",])

fig = px.scatter(data_frame=df, x=col_x, y=col_y, 
                 color="species", size='petal_length', 
                 hover_data=['petal_width'])

st.plotly_chart(fig)

st.title("Hello World")

if st.button("Click me !") : 
    st.balloons()
    
    
st.subheader("Pierre Feuille Ciseaux")

choices = ["Pierre", "Feuille", "Ciseaux"]
player_choice = st.radio("Choisissez:", choices)

if st.button("Jouer"):
    computer_choice = random.choice(choices)
    st.write(f"Vous avez choisi: {player_choice}")
    st.write(f"L'ordinateur a choisi: {computer_choice}")
    
    if player_choice == computer_choice:
        st.info("Égalité!")
    elif (player_choice == "Pierre" and computer_choice == "Ciseaux") or \
            (player_choice == "Feuille" and computer_choice == "Pierre") or \
            (player_choice == "Ciseaux" and computer_choice == "Feuille"):
        st.success("Vous avez gagné! 🎉")
    else:
        st.error("L'ordinateur a gagné!")