# pages/1_🍳_Generate_Recipe.py

import streamlit as st
from utils.recipe_helper import generate_recipe

st.title("🍳 Smart Recipe Generator")

st.markdown("Enter a list of ingredients you have, and I’ll whip up a recipe for you!")

ingredients = st.text_input("Ingredients (comma separated):", placeholder="e.g. chicken, garlic, rice")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("🍽️ Generate Recipe"):
    if ingredients.strip():
        with st.spinner("Cooking up something tasty..."):
            try:
                recipe = generate_recipe(ingredients)
                st.session_state.history.append(recipe)
                st.markdown(recipe)
            except Exception as e:
                st.error(f"⚠️ Error generating recipe: {e}")
    else:
        st.warning("Please enter some ingredients.")
