import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from IPython.display import Audio

def translate_audio(audio, target_language):
    recognizer = sr.Recognizer()
    try:
        # Recognize the speech from the audio
        text = recognizer.recognize_google(audio)
        
        # Translate the recognized text
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        return translated.text
    
    except sr.UnknownValueError:
        st.warning("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def main():
    # Multi-line heading with formatting
    st.markdown("<h1 style='text-align: center;'><strong><u>NED PGD Batch 5</u></strong></h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'><strong><u>S2S Translate & T2T Translate App</u></strong></h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Project: Muhammad Danish</h3>", unsafe_allow_html=True)
    
    # Language selection
    target_language_map = {
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Urdu": "ur",
        "Hebrew": "he",
        "Portuguese": "pt",
        "Arabic": "ar",
        "Hindi": "hi",
        "Japanese": "ja",
        "Turkish": "tr",
        "African": "af",
        "Persian": "fa"
    }
    
    target_language = st.selectbox("Select Target Language", list(target_language_map.keys()))
    
    # Voice recording
    if st.button("Record Voice Message"):
        with sr.Microphone() as source:
            st.info("Recording... Speak now.")
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
        
        st.success("Recording complete.")
        
        # Translate the recorded audio
        translated_text = translate_audio(audio, target_language_map[target_language])
        
        # Create a gTTS object for the translated text
        if translated_text:
            tts = gTTS(translated_text, lang=target_language_map[target_language])
            
            # Save the translated audio as an MP3 file
            mp3_filename = "translated_audio.mp3"
            tts.save(mp3_filename)
            
            # Display original audio and translation
            st.audio(audio.get_wav_data(), format="audio/wav")
            st.write(f"Translated Text ({target_language}): {translated_text}")
            
            # Provide an audio player for listening
            audio_player = Audio(mp3_filename, autoplay=False)
            st.write(f"Listen to Translated Audio:")
            st.write(audio_player)
            
            # Provide a download link for the translated audio
            st.markdown(f"Download Translated Audio [here](./{mp3_filename})")

if __name__ == "__main__":
    main()

