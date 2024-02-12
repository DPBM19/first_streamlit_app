import streamlit

streamlit.title('My parents new healthy diner')
streamlit.header('breakfast menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, spinach, rocket smoothie')
streamlit.text('🐔hard boiled free range egg')
streamlit.text(' 🥑🍞avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#Lets use a pick list so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberry'])
#display on the page
streamlit.dataframe(my_fruit_list)
