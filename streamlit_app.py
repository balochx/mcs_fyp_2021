# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 22:38:42 2022

@author: alishayzadag
"""

import numpy as np
import pickle
import streamlit as st
from PIL import Image

st.set_page_config(
     page_title="Pandas Real Estates' App",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://pk.linkedin.com/in/balochx',
         'Report a bug': "https://pk.linkedin.com/in/balochx",
         'About': "# An app from the students of University of Karachi"
     }
 )

st.sidebar.title('Pandas Real Estates Ltd.')
st.sidebar.write("Hello, there! :smile:")
st.sidebar.caption('Created by the UBIT folks!')

image = Image.open('pandas_real.jpg')

st.image(image, caption=None, width=500, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.caption('Image by Francesca Tosolini')

    # Loading the model
    # creating the funtion for webapp
def price_pred(input_data):
    loaded_model = pickle.load(open('trained_model2.sav', 'rb'))
    input_data_as = np.array([input_data])
    input_data_reshaped = input_data_as.reshape(1,-1)
    result = loaded_model.predict(input_data_reshaped)
    return result


def main():
    
    st.header('Pandas Real Estates App')
    
    st.subheader('Welcome to Pandas Real Estates')
    st.markdown('**We are commited to provide our clients the best possible value for their assets.**')
    st.markdown("You are very close to selling your house at a perfect value. This app will give you the recommended price for your real estate. Just enter the data given by Pandas Real Estate below. ")

    CRIM = st.number_input('Enter CRIM your value')
    ZN = st.number_input('Enter ZN value')
    INDUS = st.number_input('Enter INDUS value')
    CHAS = st.number_input('Enter CHAS value')
    NOX = st.number_input('Enter NOR value')
    RM = st.number_input('Enter RM value')
    AGE = st.number_input('Enter AGE value')
    DIS = st.number_input('Enter DIS value')
    RAD     = st.number_input('Enter RAD value')
    TAX     = st.number_input('Enter TAX value')
    PTRATIO = st.number_input('Enter PTRATION value')
    B = st.number_input('Enter B value')
    LSTAT = st.number_input('Enter LSTAT value')
        
        # fethcing the result
        
    final_result = ''
    
    if st.button('Calculate'):
            
            final_result = price_pred([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT])
                
            st.write('Recommended value for this house (in thousands(USD)):')
            st.success(final_result)
            st.balloons()
        
if __name__ == "__main__":
    main()
