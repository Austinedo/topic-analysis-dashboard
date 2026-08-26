import streamlit as st
from streamlit_theme import st_theme



LIGHT_NAV_HOVER = "#E5EBF5"
DARK_NAV_HOVER = "#24303C"


def apply_navigation_style() -> None:
    theme = st_theme()
    base = theme.get("base", "dark") if theme else "dark"

    if base == "dark":
        hover_background = DARK_NAV_HOVER
    else:
        hover_background = LIGHT_NAV_HOVER

    st.html(
        f"""
        <style>
            .local-navigation {{
                display: flex;
                flex-direction: column;
                gap: 0.15rem;
                margin: 0.25rem 0 0.9rem 0rem;
            }}

            .local-navigation a {{
                color: var(--text-color);
                display: block;
                border-radius: 0.50rem;
                font-size: 0.86rem;
                line-height: 1.35;
                margin-left: -0.35rem;
                padding: 0.35rem 0.5rem;
                text-decoration: none;
                transition:
                    background-color 150ms ease,
                    border-color 150ms ease,
                    color 150ms ease;
            }}

            .local-navigation a:hover {{
                background-color: {hover_background};
                border-left-color: var(--primary-color);
                color: var(--primary-color);
            }}

            .local-navigation a:focus {{
                background-color: {hover_background};
                border-left-color: var(--primary-color);
                color: var(--primary-color);
                outline: none;
            }}

            .local-navigation a:focus-visible {{
                background-color: {hover_background};
                border-left-color: var(--primary-color);
                color: var(--primary-color);
                outline: 2px solid var(--primary-color);
                outline-offset: 2px;
            }}

            div[data-testid="stVerticalBlock"]
            div:has(div.sticky-nav-marker) {{
                position: sticky;
                top: 6rem;
                align-self: flex-start;
                z-index: 100;
                /* max-height: calc(100vh - 2rem); */
                /* overflow-y: auto; */
                /* padding-top: 0.25rem */
            }}

            .sticky-nav-marker {{
                display: none;
            }}

            /* Allow Streamlit page-link labels to wrap instead of clipping */
            [data-testid="stPageLink"] a {{
                white-space: normal !important;
                overflow-wrap: anywhere !important;
                height: auto !important;
                /* min-height: 2.5rem; */
                align-items: flex-start !important;
            }}

            [data-testid="stPageLink"] a span {{
                white-space: normal !important;
                overflow-wrap: anywhere !important;
                text-overflow: unset !important;
                overflow: visible !important;
            }}
        </style>
        """
    )


def render_documentation_navigation() -> None:
    st.markdown(
            '<div class="sticky-nav-marker"></div>',
            unsafe_allow_html=True,
    )

    st.markdown("#### Project Overview")

    st.markdown("""
        <div class="local-navigation">
            <a href="./project-overview#problem-objective" target="_self">&emsp;▷&ensp;Problem Statement &amp; Objective</a>
            <a href="./project-overview#data-source" target="_self">&emsp;▷&ensp;Data Source &amp; Collection</a>
            <a href="./project-overview#methodology" target="_self">&emsp;▷&ensp;Methodology</a>
            <a href="./project-overview#preprocessing" target="_self">&emsp;▷&ensp;Preprocessing &amp; Representation</a>
        </div>
        """, 
        unsafe_allow_html=True)

    st.divider()

    st.markdown("#### Modeling Approaches")

    st.page_link(
        "app_pages/tfidf_kmeans_page.py",
        label="&emsp;▷&ensp;TF-IDF + K-Means",
        width="stretch",
    )

    st.page_link(
        "app_pages/sbert_kmeans_page.py",
        label="&emsp;▷&ensp;SBERT + K-Means",
        width="stretch",
    )

    st.page_link(
        "app_pages/lda_page.py",
        label="&emsp;▷&ensp;Latent Dirichlet Allocation",
        width="stretch",
    )

    st.divider()

    st.markdown("#### Conclusion")

    st.page_link(
        "app_pages/evaluation_conclusion_page.py",
        label="&emsp;▷&ensp;Evaluation & Summary",
        width="stretch",
    )