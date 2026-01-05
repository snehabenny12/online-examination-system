# Online Examination System

CLI based Online Examination System using Python.
# Online Examination System

## Project Overview
The **Online Examination System** is a Python-based web application that allows students to register, log in, and take multiple-choice exams online.  
The system provides a **secure, independent, and user-friendly platform** for conducting exams with automatic evaluation and result storage.

---

## System Workflow

1. **Login / Registration**
   - When the server starts, the login page is displayed by default.
   - New students can register using the **Register** link by providing:
     - Full Name
     - Email
     - Username
     - Password
     - Photo upload
   - After successful registration, students are redirected to the login page.
   - Only registered students can log in. Credentials are verified from the database, and a session is created for secure access.

2. **Exam Participation**
   - After login, the student is redirected to the **examination page**.
   - Exam questions are dynamically fetched from the database and displayed in **MCQ format**.
   - Students submit their answers once done.

3. **Result Evaluation**
   - The system automatically evaluates the exam by comparing answers with correct ones stored in the database.
   - The **result page** displays:
     - Score
     - Percentage
     - Pass/Fail status
   - Exam results are stored in the database for future reference.

4. **Exam Integrity**
   - Students cannot attempt the same exam multiple times.
   - If a student tries to retake the exam, a message is displayed:
     > “You have already attempted the exam.”

---

## Key Features
- **Secure login** using sessions
- **Independent student registration**
- **Dynamic question loading** from the database
- **Automatic evaluation** system
- **Result storage and display**
- **Exam reattempt restriction** to ensure fairness

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
