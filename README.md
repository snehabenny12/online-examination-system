# Online Examination System

CLI-based Online Examination System using Python.

## Overview
A Python-based application for students to **register, log in, take timed MCQ exams, and get instant results**.  
Secure login, automatic evaluation, and exam result storage ensure a real-world examination experience.

---

- Student registration and secure login  
- Dynamic MCQ exam loading from database  
- **Timed exams** with automatic submission after the timer expires  
- Automatic score calculation and result display  
- Exam reattempt restriction for fairness 

---

## Workflow
1. **Login / Register:** Students create an account or log in.  
2. **Take Exam:** Questions are fetched from the database.  
3. **Timed Exam:** A countdown timer ensures exams are completed within the allocated time.  
4. **Submit & View Result:** Score, percentage, and pass/fail status displayed automatically.  
5. **Reattempt Restriction:** Students cannot retake the same exam.

---

## Project Structure

online-exam-system/
├── manage.py
├── exam/
│ ├── models.py
│ ├── views.py
│ ├── templates/
│ └── urls.py
├── exam_project/
└── README.md

---

## Installation
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
pip install -r requirements.txt   
python manage.py runserver
