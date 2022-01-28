# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 22:38:42 2022

@author: alishayzadag
"""

import numpy as np
import pickle
import streamlit as st

    # Loading the model
    # creating the funtion for webapp
def price_pred(input_data):
    loaded_model = pickle.load(open('https://github.com/balochx/mcs_fyp_2021/trained_model2.sav', 'rb'))
    input_data_as = np.array([input_data])
    input_data_reshaped = input_data_as.reshape(1,-1)
    result = loaded_model.predict(input_data_reshaped)
    return result


def main():

    
    st.title('Pandas Real Estates')
    st.write('Welcome to Pandas Real Estates')

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
                
            st.success(final_result)
        
if __name__ == "__main__":
    main()
