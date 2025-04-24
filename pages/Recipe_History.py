# pages/2_📜_Recipe_History.py

import streamlit as st

st.title("📜 Recipe History")

if "history" not in st.session_state or not st.session_state.history:
    st.info("No recipes generated yet. Go to the Generator tab to create one.")
else:
    for i, recipe in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"### Recipe {i}")
        st.markdown(recipe)
        st.markdown("---")
