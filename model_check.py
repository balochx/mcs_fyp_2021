# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# Loading the model

def price_pred(input_data):
  #  input_data = np.array([[-0.43942006,  3.12628155, -1.12165014, -0.27288841, -1.42262747,
      # -0.24141041, -1.31238772,  2.61111401, -1.0016859 , -0.5778192 ,
   #    -0.97491834,  0.41164221, -0.86091034]])
   loaded_model = pickle.load(open('C:/Users/alishayzadag/Documents/mcs_fyp_2021/streamlit/trained_model2.sav', 'rb'))

   input_data_as = np.array([input_data])
    #reshaping the data
   input_data_reshaped = input_data_as.reshape(1,-1)
   result = loaded_model.predict(input_data_reshaped)
   
   return result

   def main():
        
        #fetching the data from the user
        CRIM = input('Enter your value')
        ZN = input('Enter your value')
        INDUS = input('Enter your value')
        CHAS = input('Enter your value')
        NOX = input('Enter your value')
        RM = input('Enter your value')
        AGE = input('Enter your value')
        DIS = input('Enter your value')
        RAD     = input('Enter your value')
        TAX     = input('Enter your value')
        PTRATIO = input('Enter your value')
        B = input('Enter your value')
        LSTAT = input('Enter your value')
        
        # fethcing the result
        
        final_result = ''
        
        final_result = price_pred([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT])
        
        print(final_result)