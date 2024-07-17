import streamlit as st
import pandas as pd

# Sample Data
FOOD_WINE_PAIRING = {
    'Beef': 'Cabernet Sauvignon',
    'Poultry': 'Chardonnay',
    'Seafood': 'Pinot Grigio',
    'Pork': 'Merlot',
    'Lamb': 'Shiraz',
}

# Convert dict to DataFrame for simplicity in subsequent steps
df = pd.DataFrame(list(FOOD_WINE_PAIRING.items()), columns=['Food', 'Wine'])

st.title('Food & Wine Pairing App')
st.markdown("This app recommends wine types based on the food you're having!")

food = st.selectbox('What are you planning to have for dinner?', df['Food'].unique())

# Confirm selection and provide wine recommendation
if st.button('Find Wine'):
    recommended_wine = df[df['Food'] == food]['Wine'].values[0]
    st.markdown(f'We recommend **{recommended_wine}** to go with {food}!')

# Page to add data to existing table
if st.checkbox('View/Add Data'):
    editable = st.checkbox('Check to Edit')
    if editable:
        st.dataframe(df, width=700, height=300)
    else:
        new_food = st.text_input("New Food", value="", max_chars=None, key=None, type='default')
        new_wine = st.text_input("New Wine", value="", max_chars=None, key=None, type='default')
        st.button('Add Pair')
        if new_food and new_wine:
            df = df.append({'Food': new_food, 'Wine': new_wine}, ignore_index=True)
            st.markdown(':wine_glass: Wine pair added! Reload page to see new entry.')

# Restricting user to make the run only on button click
if st.button('Run'):
    result= df
    st.write('Data\n' + str(result))