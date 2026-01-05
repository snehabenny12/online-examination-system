from django.shortcuts import render, redirect
from .models import Student
from .models import Question, Result
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
import json

def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        photo = request.FILES.get("photo")

        if Student.objects.filter(username=username).exists():
            return render(request, 'exam/register.html', {'error': 'Username already exists'})

        if Student.objects.filter(email=email).exists():
            return render(request, 'exam/register.html', {'error': 'Email already exists'})

        Student.objects.create(
            full_name=full_name,
            email=email,
            username=username,
            password=password,
            photo=photo
        )

        return redirect('login')

    return render(request, 'exam/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(username=username, password=password)
            request.session['student_id'] = student.id
            return redirect('exam')

        except Student.DoesNotExist:
            return render(request, 'exam/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'exam/login.html')



def exam_view(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('login')

    # ✅ Check if exam is already completed
    existing_result = Result.objects.filter(student_id=student_id).first()
    if existing_result:
        return render(request, 'exam/already_attempted.html', {
            'score': existing_result.score,
            'percentage': existing_result.percentage,
            'result': existing_result.result
        })

    # ✅ Load questions
    questions = list(Question.objects.all())
    total_questions = len(questions)

    # ✅ No questions check
    if total_questions == 0:
        return render(request, 'exam/exam.html', {
            'error': 'No questions available for the exam. Please contact administrator.',
            'no_questions': True
        })

    # ✅ Initialize exam session
    if not request.session.get('exam_started'):
        request.session['exam_started'] = True
        request.session['exam_start_time'] = timezone.now().isoformat()
        request.session['current_question'] = 0
        request.session['answers'] = {}
        request.session['exam_duration'] = 30
        request.session.set_expiry(60 * 30)

    current_question_index = request.session.get('current_question', 0)
    answers = request.session.get('answers', {})

    # ✅ Handle AJAX requests
    if request.method == "POST" and request.headers.get('Content-Type') == 'application/json':
        data = json.loads(request.body)
        action = data.get('action')

        if action == 'save_answer':
            answers[str(data['question_id'])] = data['answer']
            request.session['answers'] = answers
            return JsonResponse({'status': 'success'})

        if action == 'submit':
            return submit_exam(request, questions, answers, student_id)

    # ✅ Display current question
    question = questions[current_question_index]
    saved_answer = answers.get(str(question.id))

    return render(request, 'exam/exam.html', {
    'question': question,              # new logic
    'questions': questions,             # 👈 restore old support
    'current_index': current_question_index,
    'total_questions': total_questions,
    'saved_answer': saved_answer,
    'progress': int((current_question_index + 1) / total_questions * 100)
})



def submit_exam(request, questions, answers, student_id):
    """Helper function to submit exam and calculate results"""
    score = 0

    for question in questions:
        user_answer = answers.get(str(question.id))
        if user_answer == question.correct_answer:
            score += 1

    total = len(questions)
    percentage = (score / total) * 100 if total > 0 else 0
    result_status = "PASS" if percentage >= 50 else "FAIL"

    Result.objects.create(
        student_id=student_id,
        score=score,
        percentage=percentage,
        result=result_status
    )

    # Clear exam session
    request.session['exam_completed'] = True
    keys_to_delete = ['exam_started', 'exam_start_time', 'current_question', 'answers', 'exam_duration']
    for key in keys_to_delete:
        if key in request.session:
            del request.session[key]

    return JsonResponse({
        'status': 'submitted',
        'score': score,
        'percentage': percentage,
        'result': result_status
    })

def result_view(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('login')

    # Get the latest result for this student
    try:
        result = Result.objects.filter(student_id=student_id).latest('date_time')
        return render(request, 'exam/result.html', {
            'score': result.score,
            'percentage': result.percentage,
            'result': result.result
        })
    except Result.DoesNotExist:
        return redirect('exam')

def logout_view(request):
    # Clear all session data including exam state
    request.session.flush()
    return redirect('login')

