import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Inicializar el traductor
translator = Translator()

# Título de la aplicación
st.title('Análisis de Sentimiento con TextBlob')

st.subheader("Escribe una opinión para analizar su sentimiento")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write(
        """
        - **Polaridad**: Indica si el sentimiento es positivo, negativo o neutral, 
          con valores entre -1 (muy negativo) y 1 (muy positivo).
        - **Subjetividad**: Mide la subjetividad del contenido, entre 0 (objetivo) y 1 (subjetivo).
        """
    )

# Solicitar entrada de texto al usuario
text_input = st.text_area('Escribe tu opinión aquí:')

if text_input:
    # Traducir el texto al inglés
    translation = translator.translate(text_input, src="es", dest="en")
    trans_text = translation.text
    
    # Analizar el texto traducido
    blob = TextBlob(trans_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Mostrar los resultados
    st.write('**Polaridad:** ', round(polarity, 2))
    st.write('**Subjetividad:** ', round(subjectivity, 2))
    
    # Interpretar el sentimiento
    if polarity >= 0.5:
        st.write('**Sentimiento:** Positivo 😊')
    elif polarity <= -0.5:
        st.write('**Sentimiento:** Negativo 😔')
    else:
        st.write('**Sentimiento:** Neutral 😐')


