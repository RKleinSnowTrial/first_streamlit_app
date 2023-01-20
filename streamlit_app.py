import streamlit
#import pkg_resources
#pkg_resources.require("charset-normalizer==`2.1.1")  
#import charset-normalizer 


streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 Blue Berry Oatmeal')
streamlit.text('🥗 Kale, Spinach, and Rocket Smoothy')
streamlit.text('🐔 Hard Boild, Free-Range Eggs')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


# normalize json Text response. 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# put it in a table and make it look purty
streamlit.dataframe(fruityvice_normalized)

