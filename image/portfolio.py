import streamlit as st
import pandas as pd
import pickle
import numpy as np
import base64
import time
import tensorflow as tf
from tensorflow.keras.utils import img_to_array, load_img
from tensorflow import keras
import io
from PIL import ImageOps, Image


# @st.cache(allow_output_mutation=True)
page = st.sidebar.selectbox(
    'MENU',
    ('About Me', 'Skills', 'Projects', 'Contact')
)
if page == 'About Me':
    # st.markdown('<p class="font"> HYE LEE Portfolio </p>', unsafe_allow_html=True)
    st.title(':orange[HYE LEE] Portfolio')
    st.subheader('Data Scientist & Math Lecturer')
    # st.markdown(""" <style> .font {font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
    # </style> """, unsafe_allow_html=True)
    # st.subheader("Capable of implementing data engineering, analyzing, and visualizing : specialized in Python machine learning and regression analysis with mathematics and marketing background.")
    st.write('●	Capable of implementing data engineering, analyzing, and visualizing.')
    st.write('●	Specialized in Python machine learning and regression analysis with mathematics and marketing background.')
    st.image("ds_image.jpg")


elif page == 'Skills':
    st.title('My Skills')
    st.write("●	Programming (Python - Numpy | Scikit-Learn | Pandas | Keras | R)") 
    st.write("● Database (PSQL) | NLP | web scraping (API | json | Beautiful soup | selenium)")
    st.write("● Time Series | spatial analysis | transfer learning | convolutional neural networks")
    st.write("●	Supervised machine learning (regression | classification) | unsupervised machine learning (clustering | PCA)")
    st.write("●	Office program (MS Excel | Word | Power point) | video editor (Adobe Premiere Pro)")
    # st.image("image/download.jpeg", width= 100)
    # st.caption("Copyright Kozzi.com")

elif page == 'Projects':
    st.title('My Projects')
    st.subheader("Product Categorization Based on Product Details & Images [link](https://github.com/hlee77/capstone-4/tree/main)")
    st.write("""
    Created image/text classification model \n
    Obtained data from eBay using web API & web scraping and preprocessed data using NLP \n
    Processed and analyzed image data using transfer learning and convolutional neural networks \n
    Processed and analyzed text data using k-nearest neighbor, random Forests, logistic regression models and found the best model using grid search \n
    Created product-categorization web app using streamlit [link](https://hlee77-capstone-4-text-img-classifier-xzr8hd.streamlit.app/)
    """)
    # st.image("image/download.jpeg", width= 100)
    # st.caption("Copyright Kozzi.com")
    
    st.subheader("Mental Health and Crimes (Group)")
    st.write("Analyzed Social Impacts Using Machine Learning ") 
    st.write("Analyzed & Predicted the relationship between mental health and crimes using data from Chicago incarceration data & mental health clinic")

    st.subheader("Web APIs & NLP of Reddit.com")
    st.write("""
    Analyzed Reddit posts using web API & NLP \n
    Analyzed & Predicted classification of postings of reddit.com \n
    Scraped Reddit data using API and collected 20,000 postings \n
    Preprocessed data Using NLP \n
    Created K-Nearest Neighbor, Random Forests, Naïve Bayes Model, Logistic Regression models \n
    Found the best model using Grid Search \n
    Analyzed Social Impacts Using Machine Learning
    """) 
    # st.image("image/download.jpeg", width= 100)
    # st.caption("Copyright Kozzi.com")    

    st.subheader("Housing Price Prediction")
    st.write("""
    Analyzed housing features affecting sale price and predicted housing price \n
    Created and Refined Regression model which provides business insights
    """) 

    st.subheader("Standardized Test Analysis")
    st.write("Analyzed the effectiveness of standardized test (SAT/ACT)") 


elif page =='Contact':
    st.title("Contact Me")
    st.write("GitHub : github.com/hlee77 [link](https://github.com/hlee77)")
    st.write("LinkedIn: linkedin.com/in/hyelee7 [link](linkedin.com/in/hyelee7)")
    st.write("email : hyelee777777@gmail.com [link](hyelee777777@gmail.com)")

