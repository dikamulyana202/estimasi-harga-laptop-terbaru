import pickle
import streamlit as st

model = pickle.load(open('estimasi_laptop.sav', 'rb'))

st.title('Estimasi Harga Laptop Terbaru')

old_price = st.number_input('Input Harga Lama')
discount = st.number_input('Input Harga Diskon')
ratings = st.number_input('Input rating')
reviews = st.number_input('Input review')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[old_price, discount, ratings, reviews]]
    )
    st.write ('Estimasi harga Laptop Terbaru : ', predict)