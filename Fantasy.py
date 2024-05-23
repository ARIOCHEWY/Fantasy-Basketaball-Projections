
import streamlit as st 
from streamlit_gsheets import GSheetsConnection 
from streamlit_option_menu import option_menu
import pandas as pd
import os as os
import dotenv as dot


def app():


    #Display Title and Description 
    st.title ("Fantasy Figures")
    st.markdown("AI generated prediciton platform")


    url = "https://docs.google.com/spreadsheets/d/1lHppancL2LGW1_5vxq6D--bhsNnXpWiW3amUeASF_-g/edit?usp=sharing"

    conn = st.connection("gsheets", type=GSheetsConnection)

    projected_stats = conn.read(spreadsheet=url, worksheet="557566345")
    schedule = conn.read(spreadsheet=url, worksheet="183422182")
    top_100 = conn.read(spreadsheet=url, worksheet="138238084")
    st.dataframe(projected_stats)

    # Display Player Schedules For The EAST
    st.subheader("Player Schedules For The EAST")
    east_df = schedule[['EAST', 'Quality Games', 'Back-to-Backs', 'Max Weeks', '31-Mar', 'T3W']][schedule['EAST'].notnull()]
    st.dataframe(east_df)

    # Display Player Schedules For The WEST
    st.subheader("Player Schedules For The West")
    west_df = schedule[['WEST', 'Quality Games', 'Back-to-Backs', 'Max Weeks', '31-Mar', 'T3W']][schedule['WEST'].notnull()]
    st.dataframe(west_df)


    with st.sidebar:
        st.write("**Welcome to NBA Fantasy Figures**")
        st.caption("Here we will assist you in making projections for the upcoming NBA season")
        st.write("---------------------------------")
        # if st.button:
        
            


