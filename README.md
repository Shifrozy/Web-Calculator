# 🧮 Streamlit Calculator

A simple, interactive calculator built with [Streamlit](https://streamlit.io/).  
This web app lets you add, subtract, multiply, or divide two numbers in a clean and responsive UI.

---

## ✨ Features
- **Four Operations**: Add, Subtract, Multiply, and Divide.
- **Real-Time Results**: Instant calculation on button click.
- **Error Handling**: Friendly warning for division by zero.
- **Minimal UI**: Lightweight and mobile-friendly interface.

---

## 🚀 Demo
Run the calculator in your browser after starting the app locally.

---

## 🛠️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. **Create a Virtual Environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```
3. **Install Dependencies**
```bash
    pip install -r requirements.txt
```
    If you don’t have a requirements.txt yet, you can generate one with:
```bash
pip freeze > requirements.txt
```
4. **Run the App**
```bash
    streamlit run calculator_app.py
```

### 📁 Project Structure
```pgsql
.
├─ calculator.py       # Main Streamlit app (this file)
├─ requirements.txt    # Python dependencies (create with pip freeze)
└─ README.md           # Project documentation
```

