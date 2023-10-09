import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents new healthy diner')

streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list= pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show=my_fruit_list.loc[fruits_selected]
# Display the table on the page.

streamlit.dataframe(fruits_to_show)

def fruityvise_fun(fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvise_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvise_normalized

streamlit.header('Fruityvice Fruit Advice')

try:
  fruit_choice=streamlit.text_input('what fruit you want to choose?','kiwi')
  if not fruit_choice:
    streamlit.error('Please choose a fruit to show details')
  else:
    funct=fruityvise_fun(fruit_choice)
    streamlit.dataframe(funct)

except URLError as e:
  streamlit.error()


streamlit.header("Below is the fruits list")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row=get_fruit_load_list()
  streamlit.dataframe(my_data_row)

streamlit.stop()

fruit_choice1=streamlit.text_input('What fruit would you like to add','Raspberry')
streamlit.write('User selected', fruit_choice1)

my_cur.execute("insert into fruit_load_list values  ('from streamlit')")
