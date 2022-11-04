import streamlit as st
from stmol import showmol, render_pdb, obj_upload
import py3Dmol

st.set_page_config(layout = 'wide')

st.title('🎈 ESMfold')

uploaded_file = st.sidebar.file_uploader('Upload PDB file')

#showmol(render_pdb(id = '3EQM'))

showmol(obj_upload(uploaded_file))
