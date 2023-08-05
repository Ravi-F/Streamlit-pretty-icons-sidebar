import streamlit as st
import json
from custom_sidebar_icons import Set_Nav_Emojis as set_Nav

st.write("Package has been loaded here")

emojis_list = [ 
    {"emojiLibrary":"remix_icon","iconName":"ri-verified-badge-fill", "style":"", "elementID":""},
    {"emojiLibrary":"icon_8", "iconName":"", "emojiObject":{"src":"https://img.icons8.com/fluency/48/smiling.png", "height":50, "width":50, "alt":"smiling"}, "style":"", "elementID":"test-icon" },
    {"emojiLibrary":"tabler_icons", "iconName":"ti ti-adjustments-pin", "style":"", "elementID":"test-icon"},
    {"emojiLibrary":"Google_material_symbols", "iconName":"settings_accessibility", "style":"", "elementID":"test-icon"},
    {"emojiLibrary":"line_awesome", "iconName":"las la-dragon", "style":"", "elementID":"test-icon"},

]

emojis_render = set_Nav(emojis_list)
emojis_render.show_me_the_icons_Render()
