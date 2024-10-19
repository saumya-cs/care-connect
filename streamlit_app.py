import streamlit as st
st.set_page_config(
    page_title="My Themed App",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
    theme={
        "primaryColor": "#FF6347",
        "backgroundColor": "#F0F0F0",
        "secondaryBackgroundColor": "#FFFFFF",
        "textColor": "#000000",
        "font": "sans serif"
    }
)

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Mission", "Educational Resources", "Community Forum", "Mentor Matching"])

if page == "Mission"
  st.write("Our Mission");
  st.write("We aim to...");
