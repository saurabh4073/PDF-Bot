from flask import Flask, render_template, request, jsonify
import openai
from PyPDF2 import PdfReader
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

# Use the secret key in your application
secret_key = os.getenv("SECRET_KEY")

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = secret_key


pdf_text = ""

def parse_pdf(file_storage):
    text = ""
    with BytesIO() as pdf_buffer:
        
        file_storage.save(pdf_buffer)
        pdf_buffer.seek(0)  
        pdf_reader = PdfReader(pdf_buffer)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    global pdf_text
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    
    pdf_text = parse_pdf(file)
    return jsonify({'message': 'PDF uploaded successfully'})

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    if 'question' not in data:
        return jsonify({'error': 'No question provided'})

    print("data", data)
    question = data['question']
    global pdf_text
    print("pdf_text",pdf_text)
    
    prompt = f"{pdf_text} {question}"
    print("prompt", prompt)
    try:
        
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        print("response ", response)
        answer = response.choices[0].text.strip()
        return jsonify({'answer': answer})
    except Exception as e:
        print("error",str(e))
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
