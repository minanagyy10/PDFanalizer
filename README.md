# 📄 DocumentsSummerization


An AI-powered PDF summarizer that extracts text from PDFs and generates clear, concise summaries using the Groq API.

---

## 🚀 Features

- Upload any PDF file and get an instant AI-generated summary
- Supports text-based and scanned PDFs (via OCR)
- Fast summarization powered by **Llama 3.3 70B** through Groq
- Simple and clean Streamlit frontend
- Flask REST API backend

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | Flask |
| AI Model | Llama 3.3 70B (via Groq) |
| PDF Parsing | pdfplumber |
| OCR | Tesseract + pdf2image |

---

## 📁 Project Structure

```
pdfsummarizer/
├── backend/
│   └── app.py          # Flask API
├── frontend/
│   └── streamlit_app.py # Streamlit UI
├── .env                # API keys (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/minanagyy10/DocumentsSummerization

cd PDFanalizer
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install flask pdfplumber pdf2image pytesseract groq streamlit python-dotenv
```

### 4. Install external tools
- **Tesseract OCR** → https://github.com/UB-Mannheim/tesseract/wiki
- **Poppler** → https://github.com/oschwartz10612/poppler-windows/releases

### 5. Create `.env` file
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free API key at 👉 https://console.groq.com/keys

---

## ▶️ How to Run

### Start the backend (Flask):
```bash
cd backend
python app.py
```
Backend runs at: `http://localhost:5000`

### Start the frontend (Streamlit):
```bash
cd frontend
streamlit run streamlit_app.py
```
Frontend runs at: `http://localhost:8501`

---

## 📌 Notes

- Make sure Tesseract is installed at `C:\Program Files\Tesseract-OCR\tesseract.exe`
- Make sure Poppler is installed at `C:\poppler\Library\bin`
- Never commit your `.env` file — it's already in `.gitignore`

---

## 👤 Author

**Mina Nagy**  

