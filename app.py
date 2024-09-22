import streamlit as st

# Recipe data
recipes = {
    "Lentil Balls": {
        "ingredients": [
            "1 cup split yellow lentils (toor dal)",
            "1 tsp cumin",
            "3 garlic cloves",
            "2 green chilies",
            "Salt to taste",
            "Oil for frying or steaming"
        ],
        "procedure": [
            "Soak toor dal in water for 2 hours.",
            "Drain the water and grind the soaked lentils with cumin, garlic, and green chilies into a coarse paste. Add salt.",
            "Wet your hands and shape the mixture into small balls.",
            "Either steam the lentil balls for 10-15 minutes or deep-fry them until golden brown.",
            "Serve with chutney or curry."
        ],
        "pros": "Protein-packed, perfect for snacking or as a meal addition, can be steamed for a healthier option."
    },
    "Green Gram": {
        "ingredients": [
            "1 cup whole green gram (moong)",
            "1 onion, chopped",
            "2 tomatoes, chopped",
            "1 tsp turmeric",
            "1 tsp cumin",
            "Salt to taste",
            "Oil",
            "Water"
        ],
        "procedure": [
            "Soak whole green gram overnight.",
            "Pressure cook the soaked moong with turmeric and salt for 3 whistles.",
            "Heat oil, sauté cumin seeds, chopped onions, and tomatoes until soft.",
            "Add cooked moong and simmer for 5-10 minutes.",
            "Serve with rice or roti."
        ],
        "pros": "High in protein and fiber, excellent for digestion, and rich in essential nutrients."
    },
    "Tamarind Rice": {
        "ingredients": [
            "2 cups cooked rice",
            "1 tbsp tamarind paste",
            "2 tbsp peanuts",
            "1 tsp mustard seeds",
            "1 tsp urad dal",
            "Curry leaves",
            "2 dried red chilies",
            "1 tsp turmeric",
            "Salt to taste",
            "Oil"
        ],
        "procedure": [
            "Cook rice and let it cool.",
            "Heat oil, add mustard seeds, urad dal, dried red chilies, and curry leaves. Once they splutter, add peanuts and fry until golden.",
            "Add tamarind paste, turmeric, and salt. Simmer for 2-3 minutes.",
            "Gently fold in the cooked rice.",
            "Serve with papad or yogurt."
        ],
        "pros": "Tangy, flavorful, and easy to prepare, light yet filling."
    },
    "Lemon Rice": {
        "ingredients": [
            "2 cups cooked rice",
            "Juice of 2 lemons",
            "1 tsp mustard seeds",
            "1 tsp urad dal",
            "2 green chilies",
            "Curry leaves",
            "1 tsp turmeric",
            "Salt to taste",
            "Oil"
        ],
        "procedure": [
            "Cook the rice and let it cool slightly.",
            "In a pan, heat oil and add mustard seeds, urad dal, chopped green chilies, and curry leaves. Fry until the mustard seeds crackle.",
            "Add turmeric and salt, stir for a few seconds, then turn off the heat.",
            "Pour in the fresh lemon juice, mix well, and combine with the cooked rice.",
            "Garnish with peanuts and serve."
        ],
        "pros": "Refreshing, tangy, and full of vitamin C, quick meal option."
    },
    "Curd Rice": {
        "ingredients": [
            "2 cups cooked rice",
            "1 cup curd (yogurt)",
            "1 tsp mustard seeds",
            "1 tsp urad dal",
            "Curry leaves",
            "1 green chili",
            "Salt to taste",
            "Oil"
        ],
        "procedure": [
            "Cook rice and let it cool completely.",
            "Heat oil and add mustard seeds, urad dal, curry leaves, and chopped green chilies. Fry until they splutter.",
            "In a large bowl, mix the rice and curd until well combined. Add salt and tempering.",
            "Garnish with coriander and serve chilled or at room temperature."
        ],
        "pros": "A probiotic-rich dish that cools the body and aids digestion."
    },
    "Carrot Beans Poriyal": {
        "ingredients": [
            "1 cup chopped carrots",
            "1 cup chopped beans",
            "1 tsp mustard seeds",
            "1 tsp urad dal",
            "Curry leaves",
            "¼ cup grated coconut",
            "Salt to taste",
            "Oil"
        ],
        "procedure": [
            "Finely chop carrots and beans.",
            "Heat oil and add mustard seeds, urad dal, and curry leaves. Fry until they splutter.",
            "Add the chopped vegetables, sprinkle salt, and stir-fry on medium heat for 5-7 minutes until tender.",
            "Add grated coconut and mix well.",
            "Serve as a side dish."
        ],
        "pros": "Low-calorie, fiber-rich dish packed with vitamins."
    },
    "Tomato Rice": {
        "ingredients": [
            "2 cups cooked rice",
            "2 ripe tomatoes, chopped",
            "1 onion, chopped",
            "2 green chilies",
            "1 tsp cumin",
            "1 tsp mustard seeds",
            "Salt to taste",
            "Oil"
        ],
        "procedure": [
            "Heat oil and sauté cumin, mustard seeds, onions, and green chilies until golden.",
            "Add chopped tomatoes and cook until they become soft and pulpy.",
            "Add the cooked rice, salt, and mix well.",
            "Garnish with coriander and serve."
        ],
        "pros": "Simple, tangy, and rich in antioxidants from tomatoes."
    },
    "Egg Rice": {
        "ingredients": [
            "2 cups cooked rice",
            "2 eggs",
            "1 onion, chopped",
            "2 green chilies",
            "1 tsp soy sauce",
            "Salt to taste",
            "Oil"
        ],
        "procedure": [
            "Beat eggs with a pinch of salt and scramble in a pan, then set aside.",
            "In the same pan, sauté onions and green chilies.",
            "Add cooked rice and soy sauce, stir well. Mix in the scrambled eggs.",
            "Garnish with spring onions or coriander."
        ],
        "pros": "Quick, high in protein, and very filling."
    },
    "Chicken Gravy": {
        "ingredients": [
            "500g chicken, chopped",
            "2 onions, chopped",
            "2 tomatoes, chopped",
            "1 tbsp ginger-garlic paste",
            "1 tsp garam masala",
            "Salt to taste",
            "Oil"
        ],
        "procedure": [
            "Heat oil and sauté onions until golden. Add ginger-garlic paste and cook for a minute.",
            "Add chicken pieces and cook until browned.",
            "Add chopped tomatoes, garam masala, and salt. Simmer for 15-20 minutes until tender.",
            "Garnish with coriander and serve with rice or bread."
        ],
        "pros": "A protein-rich, flavorful dish, perfect with any meal."
    },
    "Mutton Biryani": {
        "ingredients": [
            "500g mutton, chopped",
            "2 cups basmati rice",
            "2 onions, sliced",
            "2 tomatoes, chopped",
            "1 cup yogurt",
            "2-3 green chilies",
            "Biryani masala",
            "Salt to taste",
            "Oil",
            "Mint and coriander leaves"
        ],
        "procedure": [
            "Marinate mutton with yogurt, biryani masala, ginger-garlic paste, salt, and chopped mint and coriander leaves for at least 30 minutes.",
            "Rinse and soak basmati rice for 30 minutes. Boil water, add salt, and cook the rice until it’s 70% done. Drain and set aside.",
            "In a heavy pot, heat oil, sauté onions until golden, add tomatoes, and cook until soft.",
            "Add marinated mutton, cook until browned, then cover and cook until tender (about 20-25 minutes).",
            "Layer the partially cooked rice over the mutton, sprinkle with biryani masala, and drizzle with oil or ghee. Add fried onions and extra mint and coriander leaves.",
            "Cover tightly and cook on low heat (dum) for about 30-40 minutes.",
            "Fluff gently and serve hot."
        ],
        "pros": "A delicious and aromatic dish, rich in protein and perfect for special occasions."
    },
    "Chicken Biryani": {
        "ingredients": [
            "500g chicken, chopped",
            "2 cups basmati rice",
            "2 onions, sliced",
            "2 tomatoes, chopped",
            "1 cup yogurt",
            "2-3 green chilies",
            "Biryani masala",
            "Salt to taste",
            "Oil",
            "Mint and coriander leaves"
        ],
        "procedure": [
            "Marinate chicken with yogurt, biryani masala, ginger-garlic paste, salt, and chopped mint and coriander leaves for at least 30 minutes.",
            "Rinse and soak basmati rice for 30 minutes. Boil water, add salt, and cook the rice until it’s 70% done. Drain and set aside.",
            "In a heavy pot, heat oil, sauté onions until golden, add tomatoes, and cook until soft.",
            "Add marinated chicken, cook until browned, then cover and cook until tender (about 20-25 minutes).",
            "Layer the partially cooked rice over the chicken, sprinkle with biryani masala, and drizzle with oil or ghee. Add fried onions and extra mint and coriander leaves.",
            "Cover tightly and cook on low heat (dum) for about 30-40 minutes.",
            "Fluff gently and serve hot."
        ],
        "pros": "A flavorful and filling dish, perfect for family gatherings or festive occasions."
    }
}

# Streamlit app
st.title("Bachelor Boys' Recipe App")

# Sidebar with recipe names
st.sidebar.header("Recipes")
recipe_names = list(recipes.keys())
selected_recipe = st.sidebar.selectbox("Choose a recipe:", recipe_names)

# Display recipe details
if selected_recipe:
    st.header(selected_recipe)

    st.subheader("Ingredients:")
    for ingredient in recipes[selected_recipe]["ingredients"]:
        st.write(f"- {ingredient}")

    st.subheader("Procedure:")
    for step in recipes[selected_recipe]["procedure"]:
        st.write(f"- {step}")

    st.subheader("Pros:")
    st.write(recipes[selected_recipe]["pros"])
