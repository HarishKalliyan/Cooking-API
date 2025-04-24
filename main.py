
# Smart Recipe Generator using Cohere's Command-R model

# Import necessary libraries
import streamlit as st
import cohere
import os


# Load environment variables
from dotenv import load_dotenv
load_dotenv()


# Initialize Cohere
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

# Streamlit UI
st.set_page_config(page_title="Smart Recipe Generator", page_icon="🍳")
st.title("🍳 Smart Recipe Generator")

st.markdown("Enter a list of ingredients you have, and I’ll whip up a recipe for you!")

ingredients = st.text_input("Ingredients (comma separated):", placeholder="e.g. chicken, garlic, rice")

if "history" not in st.session_state:
    st.session_state.history = []



def generate_recipe_with_cohere(ingredients):
    prompt = f"""
You are a professional chef AI. A user has these ingredients: {ingredients}.
Create a recipe with the following:
- A unique recipe name
- A short, enticing description
- A list of ingredients with measurements (use assumed defaults if needed)
- Step-by-step cooking instructions
- Estimated cook time
- Dietary tags (e.g., vegetarian, high protein, gluten-free)

Respond in markdown format.
    """

    response = co.chat(
    model="command-r",
    message=prompt,
    temperature=0.7,
    )
    return response.text


if st.button("🍽️ Generate Recipe"):
    if ingredients.strip():
        with st.spinner("Cooking up something tasty..."):
            try:
                recipe = generate_recipe_with_cohere(ingredients)
                st.session_state.history.append(recipe)
                st.markdown(recipe)
            except Exception as e:
                st.error(f"⚠️ Error generating recipe: {e}")
    else:
        st.warning("Please enter some ingredients first!")

if st.session_state.history:
    st.subheader("📜 Your Recipe History")
    for i, rec in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"### Recipe {i}")
        st.markdown("---")
        st.markdown(rec)
