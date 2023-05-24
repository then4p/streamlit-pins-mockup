import time

import streamlit as st
from PIL import Image

st.markdown("# Pauses In Speech")

st.write("_Streamlit offers file uploading_")

uploaded_file = st.file_uploader("Upload audio file to process: ", type=["mp3", "ogg", "wav"])

if uploaded_file is not None:
    # To read file as bytes:
    st.write("_...progress bars_")

    mock_progress = st.progress(0)
    for percent in range(100):
        time.sleep(0.02)
        mock_progress.progress(percent + 1)

    bytes_data = uploaded_file.getvalue()
    name = uploaded_file.name
    audio_format = name.split(".")[-1]
    st.audio(bytes_data, format=f'audio/{audio_format}')

    st.write("_...expanders_")
    image = Image.open('resources/example_wave_form.png')
    with st.expander("Show pauses"):
        st.write("_...images from bytes or files_")
        st.image(image)

    with st.expander("Show speech statistics"):
        st.write("_...columns and nice looking metrics_")
        col1, col2 = st.columns(2)
        col1.metric(label="Words per second", value=21.5, delta=-1.8)
        col2.metric(label="Average pause length", value=0.9, delta=0.15)
