import streamlit as st
from transformers import pipeline

st.title("🌐 :rainbow[Language Translation App]")

language_map = {
    "English": "en", "French": "fr", "German": "de", "Spanish": "es",
    "Italian": "it", "Portuguese": "pt", "Romanian": "ro", "Dutch": "nl",
    "Polish": "pl", "Russian": "ru", "Chinese": "zh", "Japanese": "ja",
    "Arabic": "ar", "Hindi": "hi", "Telugu": "te", "Gujarati": "gu"
}

language_names = list(language_map.keys())
input_lang_name = st.selectbox("Select Input Language:", language_names, index=0)
output_lang_name = st.selectbox("Select Output Language:", language_names, index=4) # Default to Italian

input_lang = language_map[input_lang_name]
output_lang = language_map[output_lang_name]

input_text = st.text_area("Enter text to translate:", height=150)

@st.cache_resource
def load_universal_translator():
    # This model supports 100 languages in one go!
    return pipeline("translation", model="facebook/m2m100_418M")

if st.button("Translate"):
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner(f"Translating {input_lang_name} to {output_lang_name}..."):
            try:
                translator = load_universal_translator()
                # For M2M100, we specify forced_bos_token_id for the target language
                translated = translator(input_text, src_lang=input_lang, tgt_lang=output_lang)[0]['translation_text']
                
                st.success("Translation Complete!")
                st.text_area("Translated Text:", value=translated, height=150)
            except Exception as e:
                st.error("An error occurred during translation. Please try again.")
