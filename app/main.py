import streamlit as st
import sys
import os



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

sys.path.append(BASE_DIR)

from core.services import DocumentService
from db.database import init_db

init_db()

st.set_page_config(page_title="DOCMANAGER",layout = "wide")

st.title("📁 Smart PDF Document manager")

st.divider()

tabs = st.tabs(["Upload","Search&View","Analytics"])
service = DocumentService()
with tabs[0]:

        st.header("Upload PDF")

        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
        tags = st.text_input("Tags (comma separated)")
        description = st.text_area("Description")
        lecture_date = st.date_input("Lecture Date (optional)", value=None)
        if st.button("Upload"):
            if uploaded_file:
                service.uploadDocument(uploaded_file, tags, description, lecture_date)
            else :
                st.error("Please upload a file")

with tabs[1]:
    pass

with tabs[2]:
    pass