import streamlit as st
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Mission", "Educational Resources", "Community Forum", "Mentor Matching"])
if page == "Mission"
  st.write("Our Mission");
  st.write("We aim to...");
