import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Mission", "Educational Resources", "Community Forum", "Mentor Matching"])

if page == "Mission":
  st.title('Welcome! :heart::raised_hands:');
  st.subheader("Welcome!");
  st.write("Welcome to Care Connect! This website is all about support and community - we aim to help patients find and connect with others who understand what they are going through.");
  st.subheader("Our Motivation");
  st.write("We understand that, in healthcare, mental health is key. Patients go through a lot of stress related to their illnesses - both physical and emotional.");
