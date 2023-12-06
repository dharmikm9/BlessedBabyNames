import streamlit as st
from html_elements import footer, website_title, website_desc, svg_logo


def home_page():
    # st.markdown(website_title, unsafe_allow_html=True)
    st.markdown(website_desc, unsafe_allow_html=True)
    st.markdown(footer, unsafe_allow_html=True)