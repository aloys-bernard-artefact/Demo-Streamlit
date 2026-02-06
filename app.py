import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import time 
import random
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Demo Streamlit",
    page_icon="🎨",
    layout="wide"
)

# Title and introduction
st.title("🎨 Demo Streamlit - Application Interactive")
st.markdown("""
Bienvenue dans cette application de démonstration Streamlit ! 
Explorez les différentes visualisations de données, jouez à des mini-jeux et admirez des images de chats. 🐱
""")

st.divider()

@st.cache_data()
def load_data():
    time.sleep(1.5)
    df = px.data.iris()
    return df

with st.spinner():
    df = load_data()

# Section: Graphiques interactifs
st.header("📊 Visualisations de données Iris")

# Tabs for different graph types
tab1, tab2, tab3, tab4 = st.tabs(["Scatter Plot", "Bar Chart", "Line Chart", "Histogramme"])

with tab1:
    st.subheader("Scatter Plot Interactif")
    col_x = st.select_slider("Choisis la colonne X"
                     ,options=["sepal_width", "sepal_length","petal_width", "petal_length",], key="scatter_x")
    col_y = st.select_slider("Choisis la colonne Y"
                     ,options=[ "sepal_length","sepal_width","petal_width", "petal_length",], key="scatter_y")
    
    fig = px.scatter(data_frame=df, x=col_x, y=col_y, 
                     color="species", size='petal_length', 
                     hover_data=['petal_width'],
                     title=f"Relation entre {col_x} et {col_y}")
    
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Bar Chart - Moyennes par Espèce")
    selected_col = st.selectbox("Sélectionner une mesure", 
                                ["sepal_width", "sepal_length","petal_width", "petal_length"])
    
    # Calculate means by species
    mean_by_species = df.groupby('species')[selected_col].mean().reset_index()
    
    fig_bar = px.bar(mean_by_species, x='species', y=selected_col,
                     color='species',
                     title=f"Moyenne de {selected_col} par espèce",
                     labels={'species': 'Espèce', selected_col: selected_col.replace('_', ' ').title()})
    
    st.plotly_chart(fig_bar, use_container_width=True)

with tab3:
    st.subheader("Line Chart - Tendances")
    selected_metric = st.selectbox("Sélectionner une métrique", 
                                   ["sepal_width", "sepal_length","petal_width", "petal_length"],
                                   key="line_metric")
    
    # Create line chart showing trends
    fig_line = go.Figure()
    for species in df['species'].unique():
        species_data = df[df['species'] == species].reset_index()
        fig_line.add_trace(go.Scatter(
            x=species_data.index,
            y=species_data[selected_metric],
            mode='lines+markers',
            name=species
        ))
    
    fig_line.update_layout(
        title=f"Tendance de {selected_metric} par échantillon",
        xaxis_title="Index d'échantillon",
        yaxis_title=selected_metric.replace('_', ' ').title()
    )
    
    st.plotly_chart(fig_line, use_container_width=True)

with tab4:
    st.subheader("Histogramme - Distribution")
    hist_col = st.selectbox("Sélectionner une variable", 
                           ["sepal_width", "sepal_length","petal_width", "petal_length"],
                           key="hist_col")
    
    fig_hist = px.histogram(df, x=hist_col, color='species',
                           title=f"Distribution de {hist_col}",
                           labels={hist_col: hist_col.replace('_', ' ').title()},
                           marginal="box")
    
    st.plotly_chart(fig_hist, use_container_width=True)

st.divider()

# Section: Galerie de chats
st.header("🐱 Galerie d'Images de Chats")

# Display cat images
image_dir = "images/cats"
if os.path.exists(image_dir):
    cat_images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    if cat_images:
        st.write("Admirez ces adorables chats ! 😻")
        
        # Display images in columns
        cols = st.columns(3)
        for idx, img_file in enumerate(cat_images):
            with cols[idx % 3]:
                img_path = os.path.join(image_dir, img_file)
                image = Image.open(img_path)
                st.image(image, caption=f"Chat {idx + 1}", use_container_width=True)
    else:
        st.info("Aucune image de chat trouvée dans le dossier.")
else:
    st.warning(f"Le dossier {image_dir} n'existe pas.")

st.divider()

# Section: Interactive elements
st.header("🎮 Éléments Interactifs")

st.subheader("🎈 Bouton Surprise")
if st.button("Click me !") : 
    st.balloons()
    st.text(f'Le secret est {st.secrets["db_username"]} {st.secrets["db_password"]}')

st.divider()
    
# Section: Rock Paper Scissors game
st.subheader("✊ Pierre Feuille Ciseaux")

choices = ["Pierre", "Feuille", "Ciseaux"]
player_choice = st.radio("Choisissez:", choices)

if st.button("Jouer"):
    computer_choice = random.choice(choices)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("🧑 **Vous:**")
        st.write(f"{player_choice}")
    with col2:
        st.write("🤖 **Ordinateur:**")
        st.write(f"{computer_choice}")
    
    if player_choice == computer_choice:
        st.info("Égalité! 🤝")
    elif (player_choice == "Pierre" and computer_choice == "Ciseaux") or \
            (player_choice == "Feuille" and computer_choice == "Pierre") or \
            (player_choice == "Ciseaux" and computer_choice == "Feuille"):
        st.success("Vous avez gagné! 🎉")
        st.balloons()
    else:
        st.error("L'ordinateur a gagné! 😢")