import streamlit as st
import os
import pandas as pd
import datetime
def index():
    st.session_state["index"] =True
    st.session_state["page1"] =False
    st.session_state["page2"] =False
    st.header("About this application.")
    st.markdown("Recent international standardization of accounting reporting format led to the number of reports with XBRL increase. XBRL is a generalized format of operation report: e.g., including balance sheet, investment, and operating status. In general, XBRLs contain essential information for investors and academic researchers to analyze the company's financial status. However, the XBRL file format is hard to read for humans. It, therefore, made it difficult to access companies' accounting information easily. I thus made an open-source web-application that enables easy data acquisition of accounting information disclosed on EDINET and its preprocessing.")

    st.header("How to use this application.")
    st.markdown("to be written...")

    st.header("Credit.")
    st.markdown("Author: Yuki Sato. contact: yuki.sato.f.r(at)gmail.com")
    
    st.header("Acknowledgement.")
    st.markdown("This software is composed of various open-source software: python, pandas, numpy, edinet, requests, and streamlit. We send our greatest gratitude to all contributors.")
    #with st.form(key="name-form"):
    #    st.text_input("Name", key="name")
    #    st.form_submit_button(label="Submit", on_click=change_page)

st.set_page_config(page_title="Get Data from EDINET", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
index()