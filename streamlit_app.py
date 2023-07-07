import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Pongal Sambar')
streamlit.text('Podi Idly')
streamlit.text('Poori Masal')

streamlit.header('🍌🍑 Create your own smoothie here! 🍎🥝')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
