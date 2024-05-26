import streamlit as st 
from streamlit_gsheets import GSheetsConnection 
import pandas as pd
import os as os
import dotenv as dot
import Fantasy


def app():
    
    

    st.title ("Personal me")
    Fantasy.app()



