import streamlit as st
from googletrans import Translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Descargar los datos de VADER (solo necesita hacerse una vez)
nltk.download('vader_lexicon')

# Inicializar el traductor y VADER
translator = Translator()
analyzer = SentimentIntensityAnalyzer()

# Título de la aplicación
st.title('Análisis de Sentimiento con VADER')

st.subheader("Escribe una opinión para analizar su sentimiento")

with st.sidebar:
    st.subheader("Explicación de los resultados")
    st.write(
        """
        - **Positivo**: El texto tiene una connotación positiva.
        - **Negativo**: El texto tiene una connotación negativa.
        - **Neutral**: El texto no tiene una fuerte carga emocional.
        """
    )

# Solicitar entrada de texto al usuario
text_input = st.text_area('Escribe tu opinión aquí:')

if text_input:
    # Traducir el texto al inglés
    translation = translator.translate(text_input, src="es", dest="en")
    trans_text = translation.text
    
    # Analizar el sentimiento del texto traducido con VADER
    sentiment = analyzer.polarity_scores(trans_text)
    
    # Obtener los resultados de la polaridad
    st.write('**Texto traducido:**', trans_text)
    st.write('**Polaridad:** ', sentiment['compound'])
    
    # Interpretar el sentimiento
    if sentiment['compound'] >= 0.05:
        st.write('**Sentimiento:** Positivo 😊')
    elif sentiment['compound'] <= -0.05:
        st.write('**Sentimiento:** Negativo 😔')
    else:
        st.write('**Sentimiento:** Neutral 😐')
