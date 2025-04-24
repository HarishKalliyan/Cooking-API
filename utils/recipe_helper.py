# utils/recipe_helper.py

import cohere
import os
from dotenv import load_dotenv

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def generate_recipe(ingredients: str) -> str:
    prompt = f"""
You are a professional chef AI. A user has these ingredients: {ingredients}.
Create a recipe with:
- Unique recipe name
- Short description
- List of ingredients with amounts
- Step-by-step instructions
- Estimated cook time
- Dietary tags

Return in markdown.
"""

    response = co.chat(
        model="command-r",  # command-r or command-r-plus
        message=prompt,
        temperature=0.7,
    )
    return response.text
