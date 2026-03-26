import streamlit as st
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

sys.path.append(BASE_DIR)

from db.database import init_db

init_db()

st.set_page_config(page_title="DOCMANAGER",layout = "wide")

st.title("📁 Smart PDF Document manager")

st.divider()

tabs = st.tabs(["Upload","Search&View","Analytics"])

with tabs[0]:
    pass

with tabs[1]:
    pass

with tabs[2]:
    pass