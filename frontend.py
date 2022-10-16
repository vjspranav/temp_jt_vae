import json

import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title="Junction Tree VAE ",
    page_icon=":atom:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("MolVAE")
st.sidebar.header("Navigation")
page = st.sidebar.selectbox(
    "Select a page", ["Home", "MolVAE", "BO", "Sampling", "MolOpt"]
)
if page == "Home":
    st.write("Welcome to home page")
elif page == "MolVAE":
    st.write("This is the MolVAE page")
    smiles = st.text_input("Enter SMILES")
    if st.button("Submit"):
        data = {"smiles": smiles}
        r = requests.post("http://localhost:5000/molvae", json=data)
        st.write(r.json())
elif page == "BO":
    st.write("This is the BO page")
    seed = st.text_input("Enter seed")
    if st.button("Submit"):
        data = {"seed": seed}
        r = requests.post("http://localhost:5000/bo", json=data)
        st.write(r.text.split("\n"))
elif page == "Sampling":
    st.write("This is the Sampling page")
    num = st.text_input("Enter number of samples")
    if st.button("Submit"):
        r = requests.get("http://localhost:5000/sampling?num=%s" % num)
        for line in r.text.split("\n"):
            st.write(line)
elif page == "MolOpt":
    st.sidebar.header("MolOpt")
    st.sidebar.subheader("Input SMILE")
    st.sidebar.write("COc1cc2c(cc1OC)CC([NH3+])C2")
    st.sidebar.subheader("Threshold")
    st.sidebar.write("-2.50504567445")
    st.sidebar.write("For multiple inputs give ; separated values")
    smiles = st.text_input("SMILES", value="C1=CC=CC=C1")
    st.subheader("Input Threshold")
    threshold = st.text_input("Threshold", value=0.5)
    st.subheader("Output")
    if st.button("Run"):
        data = {
            "mol": [i.strip() for i in smiles.split(";")],
            "threshold": [i.strip() for i in threshold.split(";")],
        }
        r = requests.post("http://localhost:5000/molopt", json=data)
        # make it as tables
        df = []
        t = r.text.split("\n")
        for i in range(len(t) - 2):
            temp = t[i].split("")
            print(temp)
            df.append(
                {
                    "SMILES": temp[0],
                    "Threshold": temp[1],
                    "Score": temp[2],
                    "C": temp[3],
                    "H": temp[4],
                    "N": temp[5],
                }
            )
        print(df)
        st.table(pd.DataFrame(df))
        st.write(t[-2])
