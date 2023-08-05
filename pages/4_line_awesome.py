import streamlit as st
import json
from custom_sidebar_icons import Set_Nav_Emojis as set_Nav

st.write("Package has been loaded here")

with open("./data.json", "r") as read_file:
    emojis_list = json.load(read_file)

emojis_render = set_Nav(emojis_list)
emojis_render.show_me_the_icons_Render()
