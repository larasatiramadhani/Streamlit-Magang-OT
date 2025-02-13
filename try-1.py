import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from streamlit_gsheets import GSheetsConnection
API_URL = "https://script.google.com/macros/s/AKfycbzVGKVR80ax07lH5YERo_XFP2It2bhsPAK2_L1Ke5TGpdX9k1A7TbYAllz9_zMOhg_4Lw/exec"

# Ambil data dari API
response = requests.get(API_URL)
data = response.json()
st_autorefresh(interval=10 * 1000, key="data_refresh")

# Ambil data dari API
response = requests.get(API_URL)
data = response.json()
# Konversi ke DataFrame
df = pd.DataFrame(data)
st.dataframe(df)