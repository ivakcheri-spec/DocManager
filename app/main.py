import streamlit as st
import os
import sys


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(BASE_DIR)
from db.database import init_db

from core.services import DocumentService

if "reader_mode" not in st.session_state:
    st.session_state.reader_mode = False

if "selected_doc" not in st.session_state:
    st.session_state.selected_doc = None
if "current_page" not in st.session_state:
    st.session_state.current_page = 0

init_db()

service = DocumentService()


st.set_page_config(page_title="DocManager",layout="wide")

st.title("🗂️ Smart PDF Document Manager")

st.divider()
init_db()

service = DocumentService()
st.set_page_config(page_title="DocManager",layout="wide")

tabs = st.tabs(["Upload", "Search & View", "Analytics"])

st.divider()
with tabs[0]:
    st.header("Upload PDF")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    tags = st.text_input("Tags (comma separated)")
    description = st.text_area("Description")
    lecture_date = st.date_input("Lecture Date (optional)", value=None)

    if st.button("Upload"):
        
        # if uploaded_file and tags and description:
        if uploaded_file:
            service.upload_document(uploaded_file, tags, description, lecture_date)
        else :
            st.error("Please upload a file")

with tabs[1]:
    st.header("Search & View")

    col1, col2 = st.columns(2)

    with col1:
        search_tag = st.text_input("Search by Tag")

    with col2:
        search_date = st.date_input("Search by Date", value=None)

    if st.button("Search"):
       
        st.session_state.search_results = service.search_Document(
            tags=search_tag if search_tag else None,
            date=str(search_date) if search_date else None
        )

    # TASK

        results = st.session_state.search_results

        if results and not st.session_state.reader_mode:
            st.subheader(f"Results: {len(results)} documents")
            container = st.container(height=500)

            with container:
                for doc in results:
                    # doc --> obj of Document from models.py
                    col1, col2 = st.columns([1, 3])
                    # 4 -> 25% left, 75% right

                    with col1:
                        if doc.thumbnail_path:
                            st.image(doc.thumbnail_path, width=120)

                    with col2:
                        st.write(f"**{doc.name}**")
                        st.write(f"Tags: {doc.tags}")
                        st.write(f"Description: {doc.description}")
                        st.write(f"Lecture Date: {doc.lecture_date}")

                        if st.button("Open",key=f"open_{doc.id}"):
                            st.session_state.selected_doc = doc
                            st.session_state.current_page = 0
                            st.session_state.reader_mode = True
                            st.rerun()

    if st.session_state.reader_mode and st.session_state.selected_doc:
            st.write("Reader Mode Active")
