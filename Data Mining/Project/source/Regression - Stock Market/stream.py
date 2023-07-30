import streamlit as st
import datetime
import yfinance as yf
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from plotly import graph_objs as go


st.title("Stock Prediction App")
model = load_model("trained_lstm_model.h5")


# user_date = st.date_input(label='Select the date to predict', value=None, min_value=datetime.date(2012, 4, 1))

with st.form(key='prediction_form'):
    user_date = st.date_input(label='Select the date to predict', value=None, min_value=datetime.date(2012, 4, 1))
    submit_button = st.form_submit_button(label='Predict')


def prediction(ticker):
    START = '2012-01-01'

    apple_quote = yf.download('AAPL', start = START, end = ticker)

    new_df = apple_quote.filter(['Close'])


    last_60_days = new_df[-60:].values

    scaler = MinMaxScaler(feature_range=(0,1))
    last_60_days_scaled = scaler.fit_transform(last_60_days)


    X_test = []

    X_test.append(last_60_days_scaled)
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    
    pred_price = model.predict(X_test)
    pred_price = scaler.inverse_transform(pred_price)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=apple_quote.index, y=apple_quote['Close'], name='Closing Price'))
    fig.update_layout(yaxis_title='Price in USD($)')
    fig.layout.update(title_text='Apple Stock Data', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

    st.table(apple_quote.tail(5))

    return pred_price
    
    
if submit_button:
    data_load_state = st.text("")
    pred_price = prediction(user_date)
    pred_price = str(pred_price)
    pred_price = pred_price.strip('[]')
    display_text = "The predicted price is: $" + str(pred_price)
    data_load_state.text(display_text)


