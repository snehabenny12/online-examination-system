# Online Examination System

CLI based Online Examination System using Python.
# Online Examination System

## Overview
A Python-based web application for students to **register, log in, take MCQ exams, and get instant results**.  
Secure login, automatic evaluation, and exam result storage ensure a real-world examination experience.

---

## Key Features
- Student registration and secure login  
- Dynamic MCQ exam loading from database  
- Automatic score calculation and result display  
- Exam reattempt restriction for fairness  

---

## Workflow
1. **Login / Register:** Students create an account or log in.  
2. **Take Exam:** Questions are fetched from the database.  
3. **Submit & View Result:** Score, percentage, and pass/fail status displayed.  
4. **Reattempt Restriction:** Students cannot retake the same exam.

---

## Installation
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
pip install -r requirements.txt   # if dependencies exist
python manage.py runserver
