from flask import Flask, request, jsonify
import pdfplumber
from pdf2image import convert_from_bytes
import pytesseract
import os
from groq import Groq
from dotenv import load_dotenv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\Library\bin"

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print("PDF ERROR:", e)

    if not text.strip():
        print("Switching to OCR...")
        file.seek(0)
        images = convert_from_bytes(file.read(), poppler_path=POPPLER_PATH)
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"

    print("FINAL TEXT LENGTH:", len(text))
    return text

def generate_summary(text):
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""You are an AI assistant.

Summarize this text clearly:

- Main idea
- Key points
- Conclusion

TEXT:
{text}"""
            }
        ],
        max_tokens=1024
    )
    return chat_completion.choices[0].message.content

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        if "pdf" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["pdf"]
        text = extract_text(file)

        if not text.strip():
            return jsonify({"error": "No text extracted"}), 400

        summary = generate_summary(text)
        return jsonify({"summary": summary})

    except Exception as e:
        print("BACKEND ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)