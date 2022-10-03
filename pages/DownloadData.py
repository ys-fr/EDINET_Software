import streamlit as st
import os
import pandas as pd
import datetime
import edinet
import numpy as np
from edinet.xbrl_file import XBRLDir
from edinet.xbrl_file import XBRLFile

def collectTags(path):
    path = path
    data = pd.read_csv(path,sep="\n",header=None) 
    Tags = []
    for i in data[0].values:
        i = i.split(" ")
        n = 0
        dic = {}
        N = len(i)
        for j in i:
            if len(j)==0:
                continue
            j = j.strip("<")
            if j[0]=="j":
                Tags.append(j)
            break
        pass
    Tags = np.unique(Tags)
    return Tags
    pass

def ReturnTags(Tags):
    tags = []
    dic = {i[0]:i[1] for i in pd.read_csv("Dictionary_en",header=None).values}
    for i in Tags:
        if i in dic.keys():
            tags.append([dic[i],i])
            pass
        else:
            tags.append([i,i])
    return tags
    pass

def download_data():
    kind = None
    name = None
    DataPath = None
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
        DataPath = "S100N4TI"
    with st.container():
        try:
            if DataPath!=None:
                xbrl_path = edinet.api.document.get_xbrl(DataPath, save_dir=".tmp", expand_level="file")
                xbrlfile = XBRLFile(xbrl_path)
                st.markdown("Successed")
                return xbrlfile,xbrl_path
            pass
        except:
            st.markdown("Sorry, the data is not available")
            return None
        pass

def page1():
    xbrlfile =None
    path = None
    with st.container():
        st.markdown("In this page, you can download accounting report from EDINET by filling following form.")
        pass
    with st.container():
        tab1, tab2, tab3 = st.tabs(["Download XBRL file", "Upload XBRL file", "Select file in '.tmp' directory"])

        with tab1:
            xbrlfile, path = download_data()
            st.markdown(xbrlfile!=None)
            pass
        with tab2:
            uploaded_file = st.file_uploader("Upload XBRL file")
            if uploaded_file != None:
                path = ".tmp/"+uploaded_file.name
                with open(path, 'wb') as f:
                    f.write(uploaded_file.read())
                    pass
                xbrlfile = XBRLFile(path)
                pass
            pass
        with tab3:
            Available = os.listdir(".tmp")
            path = ".tmp/"+st.selectbox('Following files are available:',Available)
            if path!=None:
                try:
                    xbrlfile = XBRLFile(path)
                    pass
                except:
                    st.markdown("Failed. Select other file")
                    pass
            pass
        pass
    
    with st.container():
        if xbrlfile!=None:
            st.markdown("# See Accounting information")
            Tags = collectTags(path)
            t = np.array(ReturnTags(Tags))
            tags = st.multiselect( 'Select tags', t[:,0])
            t = {i[0]:i[1] for i in t}
            df = []
            for i in tags:
                if xbrlfile.find(i)!=[]:
#                    st.text("{0} {1}".format(i,t[i]))
                    df.append([i, xbrlfile.find(t[i]).text])
                    pass
                else:
                    df.append([i, None])
                pass
            df = pd.DataFrame(df)
            st.dataframe(df ,use_container_width=True)
            csv = df.to_csv().encode('utf-8')
            st.download_button(
                label="Download Table",
                data=csv,
                file_name='ProcessedData.csv',
                mime='text/csv',
            )
            pass
        pass
    
st.set_page_config(page_title="Download Data from EDINET!", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.sidebar.markdown("# Download Data from EDINET")
page1()
