import streamlit as st
from streamlit_option_menu import option_menu
import Fantasy, Streaming, Personal



# Define a class to manage session state
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Create a session state object
state = SessionState(selected_app="")

def app():
    st.set_page_config(
        page_title="Main py"
    )

# class MultiApp:
#     def __init__(self):
#         self.apps = []

#     def add_app(self, title, func):
#         self.apps.append({
#             "title": title,
#             "function": func
#         })

with st.sidebar:
    # Use session state to keep track of selected app havbdfjhvasjhdsvj
    state.selected_app = option_menu(
        menu_title='Fantasy Figures',
        options=['Fantasy', 'Personal', 'Streaming'],
        icons=['house-fill', 'person-fill', 'house-fill'],
        menu_icon='chat-text-fill',
        default_index=1,
        styles={
            "container": {"padding": "5!important", "background-color": 'black'},
            "icon": {"color": "white", "font-size": "23px"},
            "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#02ab21"}
        }
    )

if state.selected_app == 'Personal':
     Personal.app()
elif state.selected_app == 'Fantasy':
     Fantasy.app()
elif state.selected_app == 'Streaming':
     Streaming.app()

