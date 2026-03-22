import streamlit as st
import google.generativeai as genai
import PyPDF2
import os
from dotenv import load_dotenv

# ------------------------------
# 1. Load the API key from .env
# ------------------------------
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    st.error("API key not found. Please add GEMINI_API_KEY to your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# ------------------------------
# 2. Set up the Gemini model
# ------------------------------
# Use gemini-2.5-flash for free tier (or gemini-1.5-flash if needed)
model = genai.GenerativeModel('gemini-2.5-flash')

# ------------------------------
# 3. Streamlit UI
# ------------------------------
st.set_page_config(page_title="PDF Summarizer", layout="centered")
st.title("📄 PDF Summarizer")
st.write("Upload a PDF and let Gemini AI summarize it for you.")

# Sidebar with author info
st.sidebar.header("About")
st.sidebar.write("Built by **Himanshu Saroha**")
st.sidebar.write("B.Tech AIML, Sharda University")
st.sidebar.write("Tools: Python, Gemini AI, Streamlit, PyPDF2")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        st.stop()

    # Display document stats
    num_pages = len(reader.pages)
    word_count = len(text.split())
    col1, col2 = st.columns(2)
    col1.metric("📄 Pages", num_pages)
    col2.metric("📝 Words", word_count)

    # Limit text to avoid hitting API token limits
    # (Gemini free tier has a limit; 3000 characters is safe)
    text_to_send = text[:3000]
    if len(text) > 3000:
        st.warning("Text truncated to 3000 characters for API limits.")

    # Summarization button
    if st.button("✨ Summarize this PDF"):
        with st.spinner("Gemini is reading your PDF..."):
            prompt = f"""
            Read the following text from a PDF document.
            Provide a clear and concise summary in 5 bullet points.
            Then give 3 key takeaways.

            Document text:
            {text_to_send}
            """
            try:
                response = model.generate_content(prompt)
                st.subheader("📌 Summary")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error generating summary: {e}")