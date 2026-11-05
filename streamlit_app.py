import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("MARKETING DASHBOARD")

# --- PASTE YOUR CLEAN SHARE LINK HERE ---
my_magic_link = "https://public.tableau.com/views/Book5_17933767307950/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

if "?" in my_magic_link:
    final_url = f"{my_magic_link}&:embed=y&:showVizHome=no"
else:
    final_url = f"{my_magic_link}?:embed=y&:showVizHome=no"

components.html(f'<iframe src="{final_url}" width="100%" height="800" frameborder="0"></iframe>', height=850)
