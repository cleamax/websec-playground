# 🔓 WebSec Playground

A deliberately vulnerable **Flask web application** to practice **Web Application Security** concepts (SQL Injection, XSS, CSRF, IDOR).  
⚠️ **For educational purposes only. Do not deploy to production.**

---

## 🎯 Purpose

This project is designed as a **hands-on security lab** for students, security enthusiasts, and developers who want to:

- Understand and exploit common **OWASP Top 10 vulnerabilities**  
- Learn how insecure coding patterns lead to real-world attacks  
- Practice **secure coding** by fixing the vulnerable endpoints  
- See how **DevSecOps tools** (Semgrep, ZAP) can be integrated into CI/CD  

---

## 🕹️ Features & Vulnerabilities

The app contains **4 main vulnerabilities**:

1. **SQL Injection (SQLi)** – insecure login form using string concatenation  
2. **Insecure Direct Object Reference (IDOR)** – profile endpoint with missing authorization check  
3. **Stored Cross-Site Scripting (XSS)** – comments section without sanitization  
4. **Cross-Site Request Forgery (CSRF)** – missing CSRF tokens on email update form  

Each vulnerability comes with:
- Example exploit scenario  
- Hints in the UI  
- Possibility to later implement a secure fix  

---

## 🛠️ Tech Stack

- **Backend:** Python 3.11, Flask, SQLite  
- **Frontend:** Jinja2 templates, basic HTML/CSS  
- **CI/CD:** GitHub Actions + Semgrep (SAST)  
- *(optional extension)*: OWASP ZAP Baseline (DAST)  

---

## 📂 Project Structure

```
websec-playground/
├─ app.py                # Flask app (vulnerable)
├─ db_init.py            # Initialize DB with demo users + seed data
├─ requirements.txt      # Python dependencies
├─ templates/            # HTML templates (deliberately unsafe rendering)
├─ static/               # CSS
└─ .github/workflows/    # CI configs (Semgrep)
```

---

## ▶️ Getting Started

1. **Clone repo & install dependencies**
   ```bash
   git clone https://github.com/<your-username>/websec-playground.git
   cd websec-playground
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Initialize the database**
   ```bash
   python db_init.py
   ```

3. **Run the app**
   ```bash
   python app.py
   ```
   → Visit: http://127.0.0.1:5000

---

## 🧨 Example Exploits

- **SQL Injection:**  
  Login with  
  ```
  username: ' OR '1'='1
  password: anything
  ```
- **IDOR:**  
  Access `/profile?id=2` to view another user's data.  
- **Stored XSS:**  
  Post a comment with:  
  ```html
  <script>alert('XSS')</script>
  ```
- **CSRF:**  
  Forge a hidden form that auto-submits a new email without the user’s consent.

---

## 🔍 CI/CD Integration

This repo includes a **GitHub Actions workflow** that runs [Semgrep](https://semgrep.dev/) against the codebase on each push/PR:

- Detects OWASP Top 10 issues  
- Uploads results as SARIF → GitHub Security tab  

*Optional:* Add [OWASP ZAP Baseline](https://www.zaproxy.org/docs/docker/baseline-scan/) for automated DAST scanning.

---

## 🧑‍💻 Learning Path

1. Explore & exploit the vulnerable endpoints  
2. Switch to a `fix/secure` branch and apply mitigations:
   - Use **parameterized queries** for SQL  
   - Implement **authorization checks** for profiles  
   - Encode/escape user input to prevent XSS  
   - Add **CSRF protection** (Flask-WTF or custom tokens)  
3. Run CI again and confirm vulnerabilities are detected/mitigated  

---

## ⚠️ Disclaimer

This application is **intentionally insecure**.  
- Do **NOT** expose it to the internet.  
- Run locally or in isolated lab environments only.  
- For **legal & educational use only**.  

---

## 📜 License

MIT – Use, modify, and share for educational purposes.  
Attribution appreciated: Created by [Max Richter](https://github.com/cleamax).

