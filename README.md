# 📄 PDF Summarizer

An intelligent PDF summarization tool powered by Google's Gemini AI and built with Streamlit. Upload any PDF document and get an instant AI-powered summary with key takeaways.

## Live Demo
[Click here to try the app](https://pdf-summarizer-hhsppnvejzceyqmnszxdqp.streamlit.app/)

## ✨ Features

- **PDF Upload & Processing**: Upload any PDF file and instantly extract text content
- **AI-Powered Summarization**: Uses Google Gemini 2.5 Flash model to generate intelligent summaries
- **Document Statistics**: View page count and word count for uploaded documents
- **Structured Output**: Gets 5 bullet-point summary plus 3 key takeaways
- **User-Friendly Interface**: Built with Streamlit for a clean, intuitive web experience
- **Safe Token Management**: Automatic text truncation to prevent API rate limiting

## 🛠️ Tech Stack

- **Python** - Core language
- **Streamlit** - Web UI framework
- **Google Generative AI** - Gemini AI for summarization
- **PyPDF2** - PDF text extraction
- **python-dotenv** - Environment variable management

## 📋 Requirements

```
streamlit
google-generativeai
PyPDF2
python-dotenv
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Google Gemini API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/himanshusarohaa/pdf-summarizer.git
   cd pdf-summarizer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   - Get your free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

### Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

1. Click "Choose a PDF file" and select your PDF
2. View the document statistics (pages and word count)
3. Click "✨ Summarize this PDF" button
4. Get your AI-generated summary with bullet points and key takeaways

## ⚙️ How It Works

1. **PDF Processing**: PyPDF2 extracts text from each page of the uploaded PDF
2. **Text Limitation**: First 3000 characters are sent to the API (respects free tier limits)
3. **AI Summarization**: Gemini generates a concise summary with:
   - 5 key bullet points
   - 3 main takeaways
4. **Display**: Results are shown in a clean, readable format

## 📊 API Limits

- The app truncates text to 3,000 characters to work within free tier limits
- Suitable for most documents and articles
- For longer documents, consider the most important pages

## 👤 About the Developer

Built by **Himanshu Saroha**  
B.Tech AIML, Sharda University

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 🔗 Links

- [GitHub Repository](https://github.com/himanshusarohaa/pdf-summarizer)
- [Google Generative AI Documentation](https://ai.google.dev/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)