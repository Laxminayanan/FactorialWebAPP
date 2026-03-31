# Factorial Web App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)

> A simple web application built using Flask that calculates the factorial of a number. 

> This project is part of my learning journey into backend development using Python and understanding how web applications actually work behind the scenes.



## 🎯 Why I Built This

I created this project to explore how Python can be used beyond scripting — especially in web development.

Instead of just writing standalone programs, I wanted to understand:

* How a backend server works
* How frontend and backend communicate
* How user input is processed in real-time
* How to structure a complete web project

This project is one of my early steps into **Flask and full-stack development using Python**.



## 🚀 Features

* Calculate factorial of any non-negative integer
* Handles invalid inputs gracefully
* Clean and minimal UI (black + yellow theme)
* Loading animation while processing
* Copy result to clipboard feature
* Client-side validation using JavaScript



## 🛠️ Tech Stack

* Backend: Python (Flask)
* Frontend: HTML, CSS, JavaScript
* Templating: Jinja2 (via Flask)



## 📂 Project Structure

```Flow
FactorialWebAPP/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```



## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Laxminayanan/FactorialWebAPP.git
cd FactorialWebAPP
```



### 2. Create a Virtual Environment

```bash
python -m venv venv
```



### 3. Activate Virtual Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On Mac/Linux:

```bash
source venv/bin/activate
```



### 4. Install Dependencies

```bash
pip install -r requirements.txt
```



### 5. Run the Application

```bash
python app.py
```



### 6. Open in Browser

Go to:

```
http://127.0.0.1:5000/
```



## 📌 Usage

1. Enter a number in the input field
2. Click on **Calculate**
3. View the result instantly
4. Click **Copy** to copy the result



## ⚠️ Input Rules

* Only integers are allowed
* Negative numbers are not supported
* Invalid input will show an error message



## 🧠 What I Learned From This Project

* Basics of Flask and routing
* Handling GET and POST requests
* Connecting backend logic with frontend UI
* Using templates (Jinja2)
* Writing cleaner project structure
* Importance of validation (client + server side)



## 💡 Future Improvements

* Add support for very large numbers (optimized logic)
* Add history of calculations
* Dark/Light theme toggle
* Convert into a REST API



## 👨‍💻 Author

This project is part of my journey in learning Python web development.
I'm actively exploring how real-world applications are built and improving step by step.

## 📜 License

This project is licensed under the MIT License.
