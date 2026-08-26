import streamlit as st

from utils.utilities import load_markdown, load_html, figure_path
from utils.navigation import apply_navigation_style, render_documentation_navigation
from utils.layout import documentation_shell


# ==========================

apply_navigation_style()
nav_column, content_column = documentation_shell()

# ==========================

with nav_column:
    render_documentation_navigation()

with content_column:

    st.title("K-Means with SBERT Semantic Embeddings")


    st.header("Approach", 
              anchor="approach", 
              divider=True)

    if approach_content := load_markdown("sbert-kmeans/sbert_approach.md"):
        st.markdown(approach_content)
    else:
        st.info("Approach content is WIP.")


    st.header("Tuning & Diagnostics", 
              anchor='tuning-diagnostics', 
              divider=True)

    st.markdown("#### < Elbow & Silhouette Score Plots >")

    if CA_figure := load_html("SBERT_KMeans_cluster_analysis.html"):
        st.iframe(CA_figure,
                  width="stretch",
                  height="content")
        st.markdown(
            "<p style='text-align: left; color: gray; font-size: 14px; margin-top: -15px;'>&ensp;Figure 1: Elbow and Silhouette Clustering Analysis plot</p>", 
            unsafe_allow_html=True
        )
    else:
        st.warning("Missing Clustering Analysis Image")

    st.markdown("#### < Silhouette Plots >")

    image_dict = {
        "2": figure_path("SBERT_KMeans_silhouette_plot_k2.png"),
        "3": figure_path("SBERT_KMeans_silhouette_plot_k3.png"),
        "4": figure_path("SBERT_KMeans_silhouette_plot_k4.png"),
        "5": figure_path("SBERT_KMeans_silhouette_plot_k5.png"),
        "6": figure_path("SBERT_KMeans_silhouette_plot_k6.png"),
        "7": figure_path("SBERT_KMeans_silhouette_plot_k7.png"),
        "8": figure_path("SBERT_KMeans_silhouette_plot_k8.png"),
        "9": figure_path("SBERT_KMeans_silhouette_plot_k9.png"),
    }

    choice = st.selectbox("Silhouette Plot -- Choose K", 
                          options=list(image_dict.keys()),
                          width=185)
    st.image(image_dict[choice], 
             width="stretch",
             caption=f"Figure 2: Silhouette Plot ({choice}) for SBERT K-Means")

    
    st.header("Model Configuration", 
              anchor="model-config", 
              divider=True)

    if model_config_content := load_markdown("sbert-kmeans/sbert_model_config.md"):
        st.markdown(model_config_content)
    else:
        st.info("Model Configuration content is WIP.")


    st.header("Clustering Results & Interpretation", 
              anchor="results-interpretation", 
              divider=True)

    if results_content := load_markdown("sbert-kmeans/sbert_results_interpretation.md"):
        st.markdown(results_content,
                    unsafe_allow_html=True)
    else:
        st.info("Results and Interpretation content is WIP.")