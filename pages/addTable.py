import streamlit as st
import pandas as pd

# Initialize session state for storing files and data frames
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = {}

# Sidebar for file uploads
st.sidebar.header("Upload your XLSX files")
uploaded_files = st.sidebar.file_uploader("Choose files", type=["xlsx"], accept_multiple_files=True)

# Check if new files are uploaded
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        if file_name not in st.session_state.uploaded_files:
            try:
                # Read the uploaded file
                df = pd.read_excel(uploaded_file)
                
                # Store the file and DataFrame in the session state
                st.session_state.uploaded_files[file_name] = df
            except Exception as e:
                st.error(f"Error reading {file_name}: {e}")

# Display a dropdown to select the file to preview
if st.session_state.uploaded_files:
    st.sidebar.header("Select file to display")
    selected_file = st.sidebar.selectbox('Select a file', list(st.session_state.uploaded_files.keys()))
    
    # Display the selected file's DataFrame
    if selected_file:
        st.write(f"Data Preview for: {selected_file}")
        st.write(st.session_state.uploaded_files[selected_file].head())

# Option to clear all uploaded files
if st.sidebar.button('Clear all files'):
    st.session_state.uploaded_files = {}

# Inform the user if no files are uploaded
else:
    st.write("Upload XLSX files to view their contents.")

