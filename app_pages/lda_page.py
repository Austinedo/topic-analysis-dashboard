import streamlit as st

from utils.utilities import load_markdown, load_html
from utils.navigation import apply_navigation_style, render_documentation_navigation
from utils.layout import documentation_shell


# ==========================

apply_navigation_style()
nav_column, content_column = documentation_shell()

# ==========================

with nav_column:
    render_documentation_navigation()

with content_column:
    st.title("Latent Dirichlet Allocation")


    st.header("Approach", 
              anchor="approach", 
              divider=True)

    if approach_content := load_markdown("lda/lda_approach.md"):
        st.markdown(approach_content)
    else:
        st.info("Approach content is WIP.")


    st.header("Tuning & Diagnostics", 
              anchor="tuning-diagnostics", 
              divider=True)

    if MCA_figure := load_html("LDA_marginalized_topic_coherence_analysis.html"):
        st.iframe(MCA_figure,
                  width="stretch",
                  height="content")
        st.markdown(
            "<p style='text-align: left; color: gray; font-size: 14px; margin-top: -15px;'>&ensp;Figure 1: C<sub>v</sub> & C<sub>umass</sub> Topic Coherence Analysis plots grouped by clusters across all model presets</p>", 
            unsafe_allow_html=True
        )
    else:
        st.warning("Missing Marginalized Clustering Analysis Interactive Figure")

    if CA_figure := load_html("LDA_topic_coherence_anaylsis_CDpreset.html"):
        st.iframe(CA_figure,
                  width="stretch",
                  height="content")
        st.markdown(
            "<p style='text-align: left; color: gray; font-size: 14px; margin-top: -15px;'>&ensp;Figure 2: C<sub>v</sub> & C<sub>umass</sub> Topic Coherence Analysis plots for the finally selected LDA model preset</p>", 
            unsafe_allow_html=True
        )
    else:
        st.warning("Missing Clustering Analysis Interactive Figure")


    st.header("Model Configuration", 
              anchor="model-config", 
              divider=True)

    if model_config_content := load_markdown("lda/lda_model_config.md"):
        st.markdown(model_config_content)
    else:
        st.info("Model Configuration content is WIP.")


    st.header("Topic Visualizations & Interpretation", 
              anchor="results-interpretation", 
              divider=True)

    # if topic_viz_content := load_html("LDA_vis_three_topic.html"):
    if topic_viz_content := load_html("LDA_pyLDAvis_dashboard.html"):
        st.iframe(topic_viz_content,
                  width="stretch",
                  height="content")
    else:
        st.warning("Missing Topic Visualization Interactive Figure")

    if results_content := load_markdown("lda/lda_results_interpretation.md"):
        st.markdown(results_content)
    else:
        st.info("Results and Interpretation content is WIP.")