#!/usr/bin/env python

## Streamlit interface for piCalc

import streamlit as st
from piCalc import easyPi, load_pi

numbers = None
output = None

def out(nums, pi_str):
    global output
    output = st.header(easyPi(nums, pi_str))

def setup():
    global numbers
    st.set_page_config(page_title="piLocator", page_icon=":pie:", layout="wide")
    with st.container():
        st.title("Find your number in Pi!")      
        st.write("Write your number in the box below, press ENTER or click somewhere in the website and get your result. ")  
        st.write("A maximum of 10 digits is set, otherwise very few results would be found.")  
        st.write("The program will give results using only integers in the text box with no symbols or letters.")
        st.write("The numbering goes from 1 onwards considering \"3\" as the digit 1 of Pi.")
        st.write("---")
        numbers = st.text_input("Input","14",10) # Maximum 10 numbers set

def main():
    global numbers
    pi_str = load_pi("piDigits/pi1e8_", 10)
    setup()
    out(numbers, pi_str)
    
if __name__ == "__main__":
    main()