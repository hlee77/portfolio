import streamlit as st
import pandas as pd
import numpy as np
import base64
import time
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
    st.subheader(':green[Data Scientist & Math Lecturer]')
    st.write("""
    - Capable of implementing data engineering, analyzing, and visualizing
    - Specialized in Python machine learning and regression analysis with mathematics and marketing background
    """)
    st.image("image/ds_image.jpg", width= 400)
    # st.caption("img src: Copyright Kozzi.com")

elif page == 'Skills':
    st.title('My Skills')
    st.write("""
    - Programming (Python - Numpy | Scikit-Learn | Pandas | Keras | R) \n
    - Database (PSQL) | NLP | web scraping (API | json | Beautiful soup | selenium)
    - Time Series | spatial analysis | transfer learning | convolutional neural networks"
    - Supervised machine learning (regression | classification) | unsupervised machine learning (clustering | PCA)
    - Office program (MS Excel | Word | Power point) | video editor (Adobe Premiere Pro)
    """)
    st.image("image/skills.jpg", width= 300)
    st.caption("img src: https://ichemeblog.org/")

elif page == 'Projects':
    st.title('My Projects')
    st.write(" ")
    st.subheader(":green[Product Categorization Model Using Texts & Images] [link](https://github.com/hlee77/capstone-4/tree/main)")
    st.image("image/capstone.JPG", width= 300)
    st.caption("img src: kozzi.com")
    st.write("""
    - Created image/text classification model \n
    - Obtained data from eBay using web API & web scraping and preprocessed data using NLP \n
    - Processed and analyzed image data using transfer learning and convolutional neural networks \n
    - Processed and analyzed text data using k-nearest neighbor, random Forests, logistic regression models and found the best model using grid search \n
    - Created product-categorization web app using streamlit [link](https://hlee77-capstone-4-text-img-classifier-xzr8hd.streamlit.app/)
    """)
    st.write(" ")
    
    st.subheader(":green[Mental Health and Crimes (Group)] [link](https://github.com/ritzba/chicago-crime-mental-health)")
    st.image("image/groupproject.JPG", width= 300)
    st.write("""
    - Analyzed Social Impacts Using Machine Learning
    - Analyzed & Predicted the relationship between mental health and crimes using data from Chicago incarceration data & mental health clinic
    """)
    st.write(" ")

    st.subheader(":green[Web APIs & NLP of Reddit.com]")
    st.image("image/redditproject.JPG", width= 300) 
    st.write("""
    - Analyzed Reddit posts using web API & NLP \n
    - Analyzed & Predicted classification of postings of reddit.com \n
    - Scraped Reddit data using API and collected 20,000 postings \n
    - Preprocessed data Using NLP \n
    - Created K-Nearest Neighbor, Random Forests, Naïve Bayes Model, Logistic Regression models \n
    - Found the best model using Grid Search \n
    - Analyzed Social Impacts Using Machine Learning
    """) 
    st.write(" ")

    st.subheader(":green[Housing Price Prediction Model]")
    st.image("image/housingprice.JPG", width= 300)
    st.write("""
    - Analyzed housing features affecting sale price and predicted housing price \n
    - Created and Refined Regression model which provides business insights
    """) 
    st.write(" ")

    st.subheader(":green[Standardized Test Analysis]")
    st.write("- Analyzed the effectiveness of standardized test (SAT/ACT)") 


elif page =='Contact':
    st.title("Contact Me")
    st.write("GitHub : github.com/hlee77 [link](https://github.com/hlee77)")
    st.write("LinkedIn: linkedin.com/in/hyelee7 [link](linkedin.com/in/hyelee7)")
    st.write("email : hyelee777777@gmail.com [link](hyelee777777@gmail.com)")