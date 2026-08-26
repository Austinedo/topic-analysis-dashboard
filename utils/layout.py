import streamlit as st



def documentation_shell():
    """ 
    Returns (navigation column, content_column)
    
    The outer columns center the combined navigation and content region
    """
    _, navigation_column, content_column, _ = st.columns([1.375, 1.375, 4.5, 2.75], gap='large')

    return navigation_column, content_column