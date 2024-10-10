import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()
st.title('Análisis de Sentimiento con TextBlob')

st.subheader("Escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write(
        """**Polaridad**: Indica si el sentimiento expresado es positivo, negativo o neutral, 
        con valores entre -1 (muy negativo) y 1 (muy positivo), donde 0 es neutral.

        **Subjetividad**: Mide cuánto del contenido es subjetivo frente a objetivo. 
        Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo."""
    )

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text_input = st.text_area('Escribe por favor: ')
    if text_input:
        # Traducir el texto al inglés para el análisis
        translation = translator.translate(text_input, src="es", dest="en")
        trans_text = translation.text
        
        # Analizar el texto traducido con TextBlob
        blob = TextBlob(trans_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Mostrar los resultados sin mostrar la traducción
        st.write('Polaridad: ', round(polarity, 2))
        st.write('Subjetividad: ', round(subjectivity, 2))
        
        # Mensaje según la polaridad
        if polarity >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
            st.audio('Kool & The Gang - Celebration.mp3', format="audio/mpeg", loop=True)
        elif polarity <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
        else:
            st.write('Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
    text_input_correction = st.text_area('Escribe por favor: ', key='4')
    if text_input_correction:
        # Realizar la corrección en inglés directamente
        blob_correction = TextBlob(text_input_correction)
        st.write("Texto corregido:", blob_correction.correct())

