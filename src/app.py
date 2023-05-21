import streamlit as st
from PIL import Image

uploaded_file = st.file_uploader("Choose a file", type=["mp3", "ogg", "wav"])
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    name = uploaded_file.name
    audio_format = name.split(".")[-1]
    st.audio(bytes_data, format=f'audio/{audio_format}')

    image = Image.open('resources/example_wave_form.png')
    st.image(image, caption='Sunrise by the mountains')
