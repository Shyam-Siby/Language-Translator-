import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit app title
st.title("Auto-Detect Language Translator")

# Input text area for the user to enter text
text_to_translate = st.text_area("Enter text to translate:")

# Language selection dictionary (including Malayalam)
languages = {'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani',
             'eu': 'Basque', 'bn': 'Bengali', 'be': 'Belarusian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'zh-cn': 'Chinese (Simplified)', 
             'zh-tw': 'Chinese (Traditional)', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English',
             'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 
             'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'iw': 'Hebrew', 'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic',
             'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada', 'ko': 'Korean', 'la': 'Latin', 
             'lv': 'Latvian', 'lt': 'Lithuanian', 'ml': 'Malayalam', 'mk': 'Macedonian', 'ms': 'Malay', 'mt': 'Maltese', 'no': 'Norwegian', 
             'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sr': 'Serbian', 
             'sk': 'Slovak', 'sl': 'Slovenian', 'es': 'Spanish', 'sw': 'Swahili', 'sv': 'Swedish', 'ta': 'Tamil', 'te': 'Telugu', 
             'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'cy': 'Welsh', 'yi': 'Yiddish'}

# Multi-select target languages
selected_languages = st.multiselect("Select target languages:", options=list(languages.values()))

# Button to translate
if st.button("Translate"):
    if text_to_translate:
        if selected_languages:
            # Translate the text into each selected language
            for target_language in selected_languages:
                target_language_code = [key for key, value in languages.items() if value == target_language][0]
                translated_text = GoogleTranslator(source='auto', target=target_language_code).translate(text_to_translate)
                
                # Display the translated text
                st.write(f"**{target_language}**: {translated_text}")
        else:
            st.write("Please select at least one target language.")
    else:
        st.write("Please enter text to translate.")
