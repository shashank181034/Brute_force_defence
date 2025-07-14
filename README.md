# 🔐 Brute Force Defense: Secure Flask Login System

A beginner-friendly **Flask web application** designed to simulate a login page protected against **brute-force attacks**.  
This project demonstrates **offensive security awareness** and **defensive techniques** using Python and Flask.

---

## 🛡️ Features

- 🔒 **Rate Limiting** — max 5 login attempts per minute per IP
- 🚫 **Account Lockout** — 3 failed attempts trigger lock
- 🤖 **Basic CAPTCHA** — blocks bot-based attacks
- 📝 **IP Logging** — logs failed login attempts with time and credentials

---

## 🧠 Why This Project?

This project is part of my cybersecurity learning journey.  
I first created a brute-force script to test a login page, and then I **defended the same app** using practical security techniques.

Built and tested on **Kali Linux**, then transferred and deployed from **Windows**.

---

## 🚀 How to Run

### 🖥️ Setup on Windows

    ```bash
    git clone https://github.com/yourusername/brute-force-defender.git
    cd brute-force-defender
    python -m venv venv
    venv\Scripts\activate
    pip install flask flask-limiter flask-session
    python app.py
Visit:
📍 http://127.0.0.1:5000

Use:

Username: admin,
Password: batman123,
CAPTCHA: 8

📦 Requirements:

Python 3.9+,
Flask,
Flask-Limiter,
Flask-Session

🔐 Bonus: I created a custom Python brute-force script to attack the app and observe vulnerabilities before adding defenses. This gave me insight into:

Login behavior under attack

How real-world bots operate

What defenses actually stop them

The script is included as brute_force.py inside the repo for learning purposes only.
