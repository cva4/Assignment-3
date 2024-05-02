import streamlit as st
import joblib

model = joblib.load("news-classification-model.pkl")
news_labels = {'0':'Technical','1':'Business','2':'sports','3':'Entertainment','4':'Polotics'}

st.title('News Classification')

user_input = st.text_area('Enter news here')

if st.button('Predict'):
    #print(user_input)
    predicted_label = model.predict([user_input])[0]
    #print('predicted Label:'+str(predicted_sentiment))

    predicted_news_label = news_labels[str(predicted_label)]

    st.info(f'Predicted sentiment: {predicted_news_label}')