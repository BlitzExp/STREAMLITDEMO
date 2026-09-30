import streamlit as st
arch = st.file_uploader("Elige archivo")
st.table(arch)