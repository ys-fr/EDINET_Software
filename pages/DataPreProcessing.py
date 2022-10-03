import streamlit as st
import os
import pandas as pd
import datetime



def page2():
    kind = None
    name = None
    with st.container():
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
    pass

st.set_page_config(page_title="Download Data from EDINET!", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.sidebar.markdown("# Download Data from EDINET")
page2()