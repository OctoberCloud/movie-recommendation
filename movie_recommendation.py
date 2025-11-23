import streamlit as st
import google.generativeai as genai

# 🔐 Load API Key securely
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="🎬 Genre-wise Entertainment Recommender", page_icon="🍿")
st.title("🎬 AI Entertainment Recommendation — Genre Wise")

genre = st.text_input("Enter a genre (Action, Thriller, Romance, Comedy, Sci-Fi, Drama, Horror, etc.):")

prompt = f"""
Recommend entertainment based ONLY on this genre: {genre}

Include 4 separate sections:
1. Movies
2. Web-Series
3. Anime
4. Books

In each section include 5 recommendations.

For every recommendation include:
- Title
- Genre
- IMDb/Rating (approx.)
- Year (for books mention published year)
- 1 line why it fits the genre

Respond clearly with headings and bullet points. Keep it clean and readable.
"""

if st.button("Recommend"):
    if genre.strip() == "":
        st.error("⚠ Please enter a genre!")
    else:
        with st.spinner("Generating recommendations… 🍿📚✨"):
            response = model.generate_content(prompt)
            result = response.text

        st.subheader("✨ Your Personalized Genre Recommendations")
        st.markdown(result)
