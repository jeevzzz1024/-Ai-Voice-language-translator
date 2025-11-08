import os
import time
import tempfile
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator
from playsound import playsound

# Global flag
isTranslation = False

# Initialize translator
translator = Translator()

# Create mapping between language names and codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    """Return the language code for a given language name."""
    return language_mapping.get(language_name, language_name)

def play_audio_gtts(text, lang):
    """Convert translated text to voice and safely play it."""
    import uuid

    try:
        # Generate unique temporary file
        temp_filename = os.path.join(tempfile.gettempdir(), f"translated_{uuid.uuid4().hex}.mp3")

        # Create and save TTS audio
        tts = gTTS(text=text, lang=lang)
        tts.save(temp_filename)

        # Play the audio
        playsound(temp_filename)

    except Exception as e:
        st.error(f"Audio playback error: {str(e)}")

    finally:
        # Try to delete after playback ends
        try:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
        except PermissionError:
            pass  # Ignore if Windows still locks it briefly

def main_process(output_placeholder, from_language, to_language):
    """Handle real-time translation and playback."""
    global isTranslation
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎙 Speak something... (Listening)")
        while isTranslation:
            try:
                # Listen to the user
                audio = recognizer.listen(source, phrase_time_limit=5)
                spoken_text = recognizer.recognize_google(audio, language=from_language)
                
                # Display what the user said
                st.write(f"🗣 You said: {spoken_text}")

                # Translate
                translated_text = translator.translate(spoken_text, src=from_language, dest=to_language).text
                
                # Display translated text
                st.success(f"🌍 Translated: {translated_text}")

                # Convert translated text to speech
                play_audio_gtts(translated_text, to_language)

            except sr.UnknownValueError:
                st.warning("😅 Could not understand. Please speak again.")
            except Exception as e:
                st.error(f"⚠ Error: {str(e)}")
                isTranslation = False

# Streamlit UI
st.title("🌐 Real-Time Language Translator Bot")

st.sidebar.markdown("---")
st.sidebar.markdown("*Developed by: Jeeva and Team 💫*")
st.sidebar.markdown("---")

# Dropdowns for selecting languages
from_language_name = st.selectbox("🎧 Select Source Language:", list(LANGUAGES.values()))
to_language_name = st.selectbox("🔊 Select Target Language:", list(LANGUAGES.values()))

# Convert names to codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Buttons
start_button = st.button("▶ Start Translation")
stop_button = st.button("⏹ Stop Translation")

# Logic for buttons
if start_button:
    if not isTranslation:
        isTranslation = True
        output_placeholder = st.empty()
        main_process(output_placeholder, from_language, to_language)

if stop_button:
    isTranslation = False
    st.warning("🛑 Translation stopped.")
