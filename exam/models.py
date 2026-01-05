from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='student_photos/')

    def __str__(self):
        return self.username

class Question(models.Model):
    question_text = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.IntegerField()
    percentage = models.FloatField()
    result = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.result}"
