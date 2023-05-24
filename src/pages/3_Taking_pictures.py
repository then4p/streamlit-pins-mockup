import streamlit as st
camera_photo = st.camera_input("Take a picture")

if camera_photo:
    st.success("Picture taken!")
    with st.expander("Show picture: "):
        st.image(camera_photo)