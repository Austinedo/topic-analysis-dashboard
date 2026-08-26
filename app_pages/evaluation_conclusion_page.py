import streamlit as st

from utils.utilities import load_markdown
from utils.navigation import apply_navigation_style, render_documentation_navigation
from utils.layout import documentation_shell


# ==========================

apply_navigation_style()
nav_column, content_column = documentation_shell()

# ==========================

with nav_column:
    render_documentation_navigation()

with content_column:

    st.title("Evaluation and Summary")


    st.header("Comparative Findings", 
              anchor="comparative-findings", 
              divider=True)

    if comp_findings_content := load_markdown("conclusion/comparative_findings.md"):
        st.markdown(comp_findings_content)
    else:
        st.info("Comparative Findings content is WIP.")


    st.header("Summary", 
              anchor="summary", 
              divider=True)

    if summary_content := load_markdown("conclusion/summary.md"):
        st.markdown(summary_content)
    else:
        st.info("Summary Content is WIP.")
