import streamlit as st

st.set_page_config(
    page_title="Landing Page",
    page_icon="uhh_favicon.ico"
)

st.write("# Welcome to my Streamlit demo! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    The markdown support lets you easily include links, images and code. 
    - Check out [streamlit.io](https://streamlit.io)
    
    :green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:    
    
"""
)
st.markdown("### But you can also show code:")

code = '''def hello():
    print("Hello, World!")'''
st.code(code, language='python')
