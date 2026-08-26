import streamlit as st

from utils.utilities import load_markdown, figure_path
from utils.navigation import render_documentation_navigation, apply_navigation_style
from utils.layout import documentation_shell

# ==========================

apply_navigation_style()
nav_column, content_column = documentation_shell()

# ==========================

with nav_column:
    render_documentation_navigation()

with content_column:
    st.header(
        "Problem Statement and Objective",
        anchor="problem-objective",
        divider=True,
    )

    if problem_content := load_markdown("overview/problem_statement_objective.md"):
        st.markdown(problem_content)
    else:
        st.info("Problem Statement and Objective content is WIP.")


    st.header(
        "Data Source and Collection",
        anchor="data-source",
        divider=True,
    )

    if data_source_content := load_markdown("overview/data_source_collection.md"):
        st.markdown(data_source_content)
    else:
        st.info("Data Source and Collection content is WIP.")


    st.header(
        "Methodology",
        anchor="methodology",
        divider=True,
    )

    workflow_figure = figure_path("analysis_workflow.png")
    if workflow_figure.exists():
        st.image(
            str(workflow_figure),
            caption="Figure: Analysis & Data Workflow",
            width='content'
        )
    else:
        st.info("Missing Analysis Workflow Image")

    if methodology_content := load_markdown("overview/methodology.md"):
        st.markdown(methodology_content)
    else:
        st.info("Methodology content is WIP.")


    st.header(
        "Data Preprocessing, Feature Extraction, and Data Representation",
        anchor="preprocessing",
        divider=True,
    )

    if preprocessing_content := load_markdown("overview/preprocessing_overview.md"):
        st.markdown(preprocessing_content)
    else:
        st.info("Preprocessing content is WIP.")