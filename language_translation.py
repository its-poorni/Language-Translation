# language_translation_app.py

import streamlit as st
from transformers import pipeline

# Set app title
st.title("🌐 :rainbow[Language Translation App]")

# Define a list of supported languages
languages = ["en", "fr", "de", "es", "it", "pt", "ro", "nl", "pl", "ru", "zh", "ja", "ar","hi","te","Gu"]

# Language selection
input_lang = st.selectbox("Select Input Language:", languages, index=0)
output_lang = st.selectbox("Select Output Language:", languages, index=1)

# Input text
input_text = st.text_area("Enter text to translate:", height=150)

# Translate button
if st.button("Translate"):
    with st.spinner("Translating..."):
        model_name = f"Helsinki-NLP/opus-mt-{input_lang}-{output_lang}"
        try:
            translator = pipeline("translation", model=model_name)
            translated = translator(input_text)[0]['translation_text']
            st.success("Translation Complete!")
            st.text_area("Translated Text:", value=translated, height=150)
        except Exception as e:
            st.error(f"Translation failed: {e}")
