import streamlit as st
import plotly.express as px

@st.cache_data()
def load_data():
    df = px.data.iris()
    return df

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