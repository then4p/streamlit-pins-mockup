import streamlit as st

uploaded_file = st.file_uploader("Choose a file", type=["mp3", "ogg", "wav"])
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    name = uploaded_file.name
    audio_format = name.split(".")[-1]
    st.audio(bytes_data, format=f'audio/{audio_format}')

# TODO image of auditok in correct width