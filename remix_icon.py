import time
import streamlit as st
from custom_sidebar_icons import Set_Nav_Emojis as set_Nav

st.set_page_config(layout="wide")

emojis_list = [ 
    {"emojiLibrary":"remix_icon","iconName":"ri-verified-badge-fill", "style":"", "elementID":""},
    {"emojiLibrary":"icon_8", "iconName":"", "emojiObject":{"src":"https://img.icons8.com/fluency/48/smiling.png", "height":50, "width":50, "alt":"smiling"}, "style":"", "elementID":"test-icon" },
    {"emojiLibrary":"tabler_icons", "iconName":"ti ti-adjustments-pin", "style":"", "elementID":"test-icon"},
    {"emojiLibrary":"Google_material_symbols", "iconName":"settings_accessibility", "style":"", "elementID":"test-icon"},
    {"emojiLibrary":"line_awesome", "iconName":"las la-dragon", "style":"", "elementID":"test-icon"},
]

emojisOrender = set_Nav(emojis_list)
emojisOrender.show_me_the_icons_Render()

if "sideNav" not in st.session_state:
    st.session_state['sideNav'] = False


query = """window.top.document.querySelectorAll("iframe[title='streamlitApp']")[0].contentDocument.head""" 

js = f"""
        <script>
             toAppend = {query}
          const GoogleEmoji = document.createElement("link");
            GoogleEmoji.href = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0";
            GoogleEmoji.rel = "stylesheet";
            toAppend.appendChild(GoogleEmoji)
           
        
            console.log({query})
        </script>
    """
st.components.v1.html(js, height=0, width=0)
# placeholder = st.empty()
# if st.session_state['sideNav'] == False:
#     with placeholder.container():
#         st.components.v1.html(js, height=0, width=0)
#         st.session_state['sideNav'] = True 
#         time.sleep(1)
#         # st.experimental_rerun()
# else:
#     placeholder.empty()

st.write("Build you MVP/App with prettier emojis")
st.write("I built this because I am currently trying to build a MVP for a start up and was displeased with the icons streamlit typically uses. Thanks to [ @jaypinho](https://discuss.streamlit.io/u/jaypinho) and [@mathcatsand ](https://discuss.streamlit.io/u/mathcatsand) from [this post](https://discuss.streamlit.io/t/top-level-links-from-a-component-iframe/36875/9) I was able to build a javascript solution to inject prettier icons.")
st.subheader("How it works:")
st.write("On the page load, we run some javascript to plant CDN links into the main HTML file to enable some icon libraries to function")
st.write("Once these are loaded, we can plant some icon tags from some pretty icon libraries like Remix and Google material symbols.")
st.write("Upon loading, this leaves a giant iframe item on the page which needs to be removed to make space for the app.")
st.write("Also, need to make sure the app does not re-plant new emojis upon reload so - when a user interacts with the page.")
st.write("Loading the function on one page will suffice but there will be instances where the user may navigate to a page via direct url rather than clicking on the tab. So best to load it on every page - to show this navigate to [here]() and [here]() and everywhere else")
st.write("Have also imposed the capability to use custom ids or use a uniform class name to customise tabs like hover color, font-style and size, spacing etc. ")
st.write("No I have not made it possible to change the page title because though we can, it won't change the path. The path will always be what streamlit deems it based on the name of the file. You could use other packages like st-pages but this seems to use url parsing. Either way, this package does not have this functionality.")
st.write("Feel free to make your own or add to the package.")
st.write("Kind thanks to [ @jaypinho](https://discuss.streamlit.io/u/jaypinho) and [@mathcatsand ](https://discuss.streamlit.io/u/mathcatsand) and the community")

code = """
        from custom_sidebar_icons import Set_Nav_Emojis as set_Nav

        Data = [ 
            {"emojiLibrary":"remix_icon","iconName":"ri-verified-badge-fill", "style":"", "elementID":"",}',
            {"emojiLibrary":"icon_8", "iconName":"", "emojiObject":{'src':"https://img.icons8.com/fluency/48/smiling.png", 'height':50, 'width':50, 'alt':'smiling'}, "style":"", "elementID":"test-icon" },'
            {"emojiLibrary":"tabler_icons", "iconName":"ti ti-adjustments-pin", "style":"", "elementID":"test-icon"},'
            {"emojiLibrary":"Google_material_symbols", "iconName":"settings_accessibility", "style":"", "elementID":"test-icon"},'
            {"emojiLibrary":"line_awesome", "iconName":"las la-dragon", "style":"", "elementID":"test-icon"},
            ]

        emojis_render = set_Nav(Data)
        emojis_render.show_me_the_icons_Render()

        # Also load this function unto every page if you wish to use custom css - it makes sure on page click, the class names are appended to the elements. Place it at the top before any other code is run
        emoji_render.create_unique_class_for_streamlitTabs_()
    """
st.code(code, language='python')

icon_urls = [
    "https://icons8.com/icons/",
    "https://remixicon.com/",
    "https://icons8.com/line-awesome",
    "https://tabler-icons.io/",
    "https://fonts.google.com/icons", 
]

st.subheader("Icon Urls:")
for url in icon_urls:
    st.markdown(url)










