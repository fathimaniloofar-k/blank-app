import streamlit as st
import streamlit.components.v1 as components

# 1. Make the page wide so your charts have lots of room!
st.set_page_config(layout="wide")

st.title("Welcome to My Cool Lego Tower!")

# 2. This is your personal magic link to your dashboard
my_magic_link = "https://public.tableau.com/views/Book5_17933767307950/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# 3. Clean up the link parameters automatically
if "?" in my_magic_link:
    final_url = f"{my_magic_link}&:embed=y&:showVizHome=no"
else:
    final_url = f"{my_magic_link}?:embed=y&:showVizHome=no"

# 4. Open the window frame to show your interactive project!
components.html(f'<iframe src="{final_url}" width="100%" height="800" frameborder="0"></iframe>', height=850)
