# WebSec Playground

A deliberately vulnerable **Flask-based web application** for hands-on learning of **web application security** concepts such as SQL Injection, XSS, CSRF, and IDOR.

> **Educational use only.** This project is intentionally insecure and must not be deployed to production environments.

---

## Overview

WebSec Playground is a local security lab designed to help developers and security practitioners:

- Understand common **OWASP Top 10** vulnerabilities
- Observe how insecure coding patterns lead to real-world exploits
- Practice **secure coding** by mitigating vulnerabilities
- Learn how **DevSecOps tooling** (SAST/DAST) integrates into CI pipelines

The project emphasizes both **offensive understanding** and **defensive remediation**, reflecting real-world security engineering workflows.

---

## Included Vulnerabilities

The application intentionally includes the following vulnerability classes:

1. **SQL Injection (SQLi)**  
   Insecure authentication logic using string-concatenated SQL queries.

2. **Insecure Direct Object Reference (IDOR)**  
   Missing authorization checks on user profile access.

3. **Stored Cross-Site Scripting (XSS)**  
   Unsanitized user input rendered in comment functionality.

4. **Cross-Site Request Forgery (CSRF)**  
   State-changing request without CSRF protection.

Each vulnerability is:
- Reproducible via basic interaction
- Accompanied by contextual hints
- Intended to be fixed as part of the learning process

---

## Technology Stack

- **Backend:** Python 3.11, Flask, SQLite
- **Frontend:** Jinja2 templates, HTML/CSS
- **Security Tooling:**
  - Semgrep (SAST) via GitHub Actions
  - Optional: OWASP ZAP Baseline (DAST)

---

## Project Structure

```text
websec-playground/
├── app.py                # Vulnerable Flask application
├── db_init.py            # Database initialization and seed data
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates (intentionally unsafe)
├── static/               # Static assets (CSS)
└── .github/workflows/    # CI configuration (Semgrep)
```

--- 

Getting Started
1) Clone the repository and install dependencies
git clone https://github.com/cleamax/websec-playground.git
cd websec-playground

python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt

2) Initialize the database
python db_init.py

3) Run the application
python app.py


The application will be available at:
http://127.0.0.1:5000

Example Attack Scenarios

The following examples illustrate the intended learning surface.
Use only in local or isolated lab environments.

SQL Injection (SQLi)
username: ' OR '1'='1
password: any

Insecure Direct Object Reference (IDOR)

Access another user’s profile by modifying the query parameter:

/profile?id=2

Stored Cross-Site Scripting (XSS)
<script>alert('XSS')</script>

Cross-Site Request Forgery (CSRF)

Forge a malicious form that submits a state-changing request
(e.g. an email update) without the user’s consent.

CI / Security Scanning

This repository includes a GitHub Actions workflow that runs Semgrep
on each push and pull request:

Static Application Security Testing (SAST)

Detection of common OWASP Top 10 vulnerability patterns

SARIF output integrated into the GitHub Security tab

Optional extension: integrate OWASP ZAP Baseline for automated
Dynamic Application Security Testing (DAST).

Recommended Learning Workflow

Explore the application and identify vulnerabilities

Exploit the issues to understand their impact

Apply mitigations in a dedicated secure or fix branch:

Parameterized SQL queries

Proper authorization checks

Output encoding and input validation

CSRF protection mechanisms

Re-run CI and verify that findings are reduced or eliminated

Security Notice

This project is intentionally insecure.

Do not deploy or expose it to the public internet

Run only in local or isolated environments

Use strictly for educational and research purposes

License

MIT License.

Created by Max Richter
.


