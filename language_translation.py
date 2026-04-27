import streamlit as st
from transformers import pipeline

# Set app title
st.title("🌐 :rainbow[Language Translation App]")

# Mapping full names to ISO codes for the model
language_map = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Dutch": "nl",
    "Polish": "pl",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
    "Hindi": "hi",
    "Telugu": "te",
    "Gujarati": "gu"
}

# Get list of full names for the UI
language_names = list(language_map.keys())

# Language selection using full names
input_lang_name = st.selectbox("Select Input Language:", language_names, index=0)
output_lang_name = st.selectbox("Select Output Language:", language_names, index=1)

# Convert names back to codes for the NLP model
input_lang = language_map[input_lang_name]
output_lang = language_map[output_lang_name]

# Input text
input_text = st.text_area("Enter text to translate:", height=150)

# Optimization: Cache the model so it only loads once
@st.cache_resource
def load_translator(model_name, task_name):
    return pipeline(task_name, model=model_name)

# Translate button
if st.button("Translate"):
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner(f"Translating from {input_lang_name} to {output_lang_name}..."):
            model_name = f"Helsinki-NLP/opus-mt-{input_lang}-{output_lang}"
            task_name = f"translation_{input_lang}_to_{output_lang}"
            
            try:
                translator = load_translator(model_name, task_name)
                translated = translator(input_text)[0]['translation_text']
                
                st.success("Translation Complete!")
                st.text_area("Translated Text:", value=translated, height=150)
                
            except Exception:
                st.error(f"The translation pair {input_lang_name} ➔ {output_lang_name} is not currently supported by this model.")
