import streamlit as st
import os
import pandas as pd
import datetime
st.set_page_config(page_title="Get Data from EDINET", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
# 0: DocID, 1: CompanyName, 2: year
data = pd.read_csv("CurrentAvailableData.csv",header=None,index_col=None)
AvailableData = {i[1]:[i[0],i[2]] for i in data.values}
os.listdir("Data")
st.session_state["index"] =True
st.session_state["page1"] =False
st.session_state["page2"] =False

def index():
    st.session_state["index"] =True
    st.session_state["page1"] =False
    st.session_state["page2"] =False
    st.header("About this application.")
    st.markdown("Recent international standardization of accounting reporting format led to the number of reports with XBRL increase. XBRL is a generalized format of operation report: e.g., including balance sheet, investment, and operating status. In general, XBRLs contain essential information for investors and academic researchers to analyze the company's financial status. However, the XBRL file format is hard to read for humans. It, therefore, made it difficult to access companies' accounting information easily. I thus made an open-source software that enables easy data acquisition of accounting information disclosed on EDINET and its preprocessing.")

    st.header("How to use this application.")
    st.markdown("to be written...")

    st.header("Credit.")
    st.markdown("Author: Yuki Sato. contact: yuki.sato.f.r(at)gmail.com")

    st.header("Acknowledgement.")
    st.markdown("This software is composed of various open-source software: python, pandas, numpy, edinet, xbrr, requests, and streamlit. We send our greatest gratitude to all contributors to that software.")
    #with st.form(key="name-form"):
    #    st.text_input("Name", key="name")
    #    st.form_submit_button(label="Submit", on_click=change_page)

def page1():
    st.session_state["index"] =False
    st.session_state["page1"] =True
    st.session_state["page2"] =False
    kind = None
    name = None
    with st.container():
        st.header("Download Data from EDINET!")
        st.markdown("In this page, you can download accounting report from EDINET by filling following form.")

    with st.container():
        st.subheader("Please fill in following form")
        col1, col2 = st.columns(2)
        # select company
        with col1:
            st.markdown("##### Select company")
            st.markdown("Please input the company name or ticker code you want to download on the following form.")
            st.markdown("Currently available data can see from A.")
            kind = st.radio(
            "Input",
            ('Company name', 'Tieker code'))
            pass
        # select year
        with col2:
            st.markdown("##### Select year")
            now = datetime.datetime.now()
            year = now.year
            st.markdown("EDINET allows us to download data at most five years before (from {1}/{2}/{0} to {4}/{5}/{3}).".format(now.year-5,now.month,now.day,now.year,now.month,now.day) )
            pass
    with st.container():
        col1, col2 = st.columns(2)
        # select company
        with col1:
            if kind == "Company name":
                name = st.text_input("Fill in the company name")
                pass
            else:
                name = st.text_input("Fill in the ticker code" )
                pass
            pass
        # select year
        with col2:
            options = st.multiselect( 'Select year', [i for i in range(year-5,year+1,1)],  [year])
            pass
    with st.container():
        st.header("Following data is available")
        if kind !=None:
            st.dataframe(pd.DataFrame([[1,2,3],[1,2,3]]) ,use_container_width=True)
            pass
        st.text(name)
        st.text(options)
    with st.container():
        st.write("dsafas")
        
    
    #with st.form(key="name-form"):
    #    st.text_input("Name", key="name")
    #    st.form_submit_button(label="Submit", on_click=change_page)
    
def page2():
    st.session_state["index"] =False
    st.session_state["page1"] =False
    st.session_state["page2"] =True
    st.title("See Company Info")
    st.text_input("Name", key="name")

pages = dict(
    page1="Download Data",
    page2="See Company Info",
)
index()
#page1()
#page_id = st.sidebar.selectbox( # st.sidebar.*でサイドバーに表示する
#    "ページ名",
#    ["Download Data", "See Company Info"],
#)
with st.sidebar:
    st.caption("Index")
    st.markdown("[Home](page1)")
    st.markdown("[Download Data](page1)")
    st.markdown("[Get information from XBRL](page1)")

#if page_id == "Download Data":
#    page1()

#if page_id == "See Company Info":
#    page2()