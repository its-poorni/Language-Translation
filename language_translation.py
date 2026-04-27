import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="🌐 Translator", layout="centered")

# ----------- CUSTOM CSS -----------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1f4037, #99f2c8);
    }

    .main {
        background: transparent;
    }

    .app-card {
        background: rgba(255, 255, 255, 0.15);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0px 8px 32px rgba(0,0,0,0.2);
    }

    h1 {
        text-align: center;
        color: white;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, #ff9966, #ff5e62);
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 10px;
        border: none;
    }

    .stTextArea textarea {
        border-radius: 10px;
    }

    .stSelectbox div {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- UI CARD START -----------
st.markdown('<div class="app-card">', unsafe_allow_html=True)

st.title("🌐 Language Translator")

language_map = {
    "English": "en", "French": "fr", "German": "de", "Spanish": "es",
    "Italian": "it", "Portuguese": "pt", "Romanian": "ro", "Dutch": "nl",
    "Polish": "pl", "Russian": "ru", "Chinese": "zh", "Japanese": "ja",
    "Arabic": "ar", "Hindi": "hi", "Telugu": "te", "Gujarati": "gu"
}

col1, col2 = st.columns(2)

with col1:
    input_lang_name = st.selectbox("From", list(language_map.keys()))

with col2:
    output_lang_name = st.selectbox("To", list(language_map.keys()), index=4)

input_lang = language_map[input_lang_name]
output_lang = language_map[output_lang_name]

input_text = st.text_area("Enter text", height=150)

@st.cache_resource
def load_model():
    return pipeline("translation", model="facebook/m2m100_418M")

if st.button("✨ Translate Now"):
    if input_lang == output_lang:
        st.warning("Choose different languages.")
    elif not input_text.strip():
        st.warning("Enter some text.")
    else:
        with st.spinner("Translating..."):
            translator = load_model()
            result = translator(input_text, src_lang=input_lang, tgt_lang=output_lang)
            translated = result[0]['translation_text']

            st.success("Done ✅")
            st.text_area("Translated Text", translated, height=150)

st.markdown('</div>', unsafe_allow_html=True)
