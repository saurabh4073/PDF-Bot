# PDF Chatbot
This repository contains a Flask web application that serves as a PDF chatbot. The application allows users to upload PDF files, ask questions related to the content of the PDF, and receive AI-generated answers using the OpenAI GPT-3.5 model. The backend is built with Flask and integrates with the OpenAI API for natural language processing. The frontend is designed with HTML, CSS (Bootstrap), and JavaScript. Additionally, the project utilizes a .env file for environment variables and a .gitignore file to exclude sensitive information and unnecessary files from version control.

## Installation
1. Clone the repository:
``` 
    git clone https://github.com/saurabh4073/PDF-Bot.git
```
2. Required Changes: <br>
    2. Add .env file and add OpenAI key for it ass follows-
    ```
    SECRET_KEY="<Your key>"
    ```  
## Usage
Run using the following command:
```
    python app.py
```

open in browser the following link:
```
    http://127.0.0.1:5000
```

## Working with Screenshots
Add the pdf file in the upload file option and then put questions to be answered by the app.
![image](https://github.com/saurabh4073/PDF-Bot/assets/49804941/321d0784-6b50-4c90-b9c6-4f60e0ad44d5)

## Acknowledgments
This project was inspired by an Idea of friend to get details from PDF.