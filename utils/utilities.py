from pathlib import Path
import pandas as pd
import streamlit as st



ROOT = Path(__file__).resolve().parents[1]

ARTIFACTS = ROOT / "artifacts"
FIGURES = ARTIFACTS / "figures"
INTERACTIVE = ARTIFACTS / "interactive"
TABLES = ARTIFACTS / "tables"
TEXT = ARTIFACTS / "texts"

STYLESHEET = ROOT / "utils" / "styles.css"

@st.cache_data
def load_csv(filename: str) -> pd.DataFrame:
    path = TABLES / filename

    if not path.exists():
        return None
    
    return pd.read_csv(path)


@st.cache_data
def load_markdown(filename: str) -> str:
    path = TEXT / filename

    if not path.exists():
        return None
    
    return path.read_text(encoding="utf-8")


@st.cache_data
def load_html(filename: str) -> str:
    path = INTERACTIVE / filename

    if not path.exists():
        return None
    
    return path.read_text(encoding="utf-8")


def figure_path(filename: str) -> Path:
    return FIGURES / filename

@st.cache_data
def load_stylesheet() -> str:
    return STYLESHEET.read_text(encoding='utf-8')

def apply_global_styles() -> None:
    st.html(f"<style>{load_stylesheet()}</style>")
