import streamlit as st
from googletrans import Translator
from textblob import TextBlob

# Inicializar el traductor
translator = Translator()

# Título de la aplicación
st.title('Análisis de Sentimiento para Texto en Español')

st.subheader("Escribe una opinión en español para analizar su sentimiento")

# Solicitar entrada de texto al usuario
text_input = st.text_area('Escribe tu opinión aquí:')

if text_input:
    # Traducir el texto al inglés internamente
    translation = translator.translate(text_input, src="es", dest="en")
    trans_text = translation.text
    
    # Crear un objeto TextBlob con el texto traducido
    blob = TextBlob(trans_text)
    
    # Obtener los valores de polaridad y subjetividad
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Mostrar los resultados
    st.write(f"**Polaridad:** {polarity}")
    st.write(f"**Subjetividad:** {subjectivity}")
    
    # Determinar el sentimiento basado en la polaridad
    if polarity > 0.1:  # Ajuste para detectar positivo
        st.write("**Sentimiento:** Positivo 😊")
    elif polarity < -0.1:  # Ajuste para detectar negativo
        st.write("**Sentimiento:** Negativo 😔")
    else:
        st.write("**Sentimiento:** Neutral 😐")
