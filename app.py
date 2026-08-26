import streamlit as st

from utils.utilities import apply_global_styles



st.set_page_config(
    page_title="Business Reviews Topic Modeling Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_global_styles()

pages = [
    st.Page(
        "app_pages/landing_page.py",
        title="Home",
        default=True,
    ),
    st.Page(
        "app_pages/overview_page.py",
        title="Project Overview",
        url_path="project-overview",
    ),
    st.Page(
        "app_pages/tfidf_kmeans_page.py",
        title="▷ TF-IDF + K-Means",
        url_path="tfidf-kmeans",
    ),
    st.Page(
        "app_pages/sbert_kmeans_page.py",
        title="▷ SBERT + K-Means",
        url_path="sbert-kmeans",
    ),
    st.Page(
        "app_pages/lda_page.py",
        title="▷ Latent Dirichlet Allocation",
        url_path="lda",
    ),
    st.Page(
        "app_pages/evaluation_conclusion_page.py",
        title="▷ Evaluation & Conclusion",
        url_path="conclusion",
    ),
]

selected_page = st.navigation(pages, position="hidden")
selected_page.run()