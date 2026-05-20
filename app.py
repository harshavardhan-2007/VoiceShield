import streamlit as st
import whisper
from detector import detect_scam
model=whisper.load_model("base")
st.title("VoiceShield AI")
st.write("Upload a voice call recording to detect scams ")
upload_file=st.file_uploader("Upload audio",type=["mp3","wav"])
if upload_file:
    with open("temp_audio.wav","wb") as f:
        f.write(upload_file.read())
    st.write("Transcribing audio.....")
    result=model.transcribe("temp_audio.wav")
    text=result["text"]
    st.subheader("Transcript")
    st.write(text)
    risk,score,found=detect_scam(text)
    st.subheader("Detection Report!")
    st.write(f"Risk Level: {risk}")
    st.write(f"Risk Score: {score}")
    st.write(f"Detection Keywords: {found}")