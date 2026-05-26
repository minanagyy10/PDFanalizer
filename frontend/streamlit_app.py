import streamlit as st
import requests
 
st.title("📄 AI PDF Summarizer")
 
file = st.file_uploader("Upload PDF", type=["pdf"])
 
if file:
 
    with st.spinner("Processing..."):
 
        response = requests.post(
            "http://127.0.0.1:5000/summarize",
            files={"pdf": file}
        )
 
        try:
            data = response.json()
        except Exception:
            st.error("Server did not return valid JSON")
            st.write("Raw Response:", response.text)
            st.stop()
 
        if "summary" in data:
            st.success("Done!")
            st.write(data["summary"])
        else:
            st.error(data.get("error", "Unknown error"))
 
