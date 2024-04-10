import streamlit as st
import pandas as pd

# Load the data
@st.cache
def load_data():
    data = pd.read_csv("car_data.csv")
    return data

data = load_data()

# Sidebar
st.sidebar.header('Filter Options')

car_name = st.sidebar.text_input('Car Name')
transmission = st.sidebar.multiselect('Transmission', options=['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))
year_range = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))

if st.sidebar.button('Submit'):
    # Apply filters
    filtered_data = data.copy()
    if car_name:
        filtered_data = filtered_data[filtered_data['car_name'].str.contains(car_name, case=False)]
    if transmission:
        filtered_data = filtered_data[filtered_data['transmission'].isin(transmission)]
    filtered_data = filtered_data[(filtered_data['selling_price'] >= selling_price_range[0]) & (filtered_data['selling_price'] <= selling_price_range[1])]
    filtered_data = filtered_data[(filtered_data['year'] >= year_range[0]) & (filtered_data['year'] <= year_range[1])]
    
    # Display the filtered data
    st.write(filtered_data)
else:
    # Display original data
    st.write(data)
