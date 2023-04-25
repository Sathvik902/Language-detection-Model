import pickle
import string
import streamlit as st
import webbrowser


global LRDmodel

file1 = open('model.pckl','rb')
Model = pickle.load(file1)
file1.close()

st.title("Language Detection Model")
input_test = st.text_input("Provide your Text input Here","Hello!, I am sathvik")


button_clicked = st.button('Get Language Name')
if button_clicked:
  st.text(Model.predict([input_test]))

  
  
  
  
  
