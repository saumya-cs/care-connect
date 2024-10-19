import streamlit as st
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Mission", "Educational Resources", "Community Forum", "Mentor Matching"])
st.set_page_config(
    page_title= "Care Connect",
    page_icon= "🤝",
    layout= "center",
    initial_sidebar_state="auto",
)
