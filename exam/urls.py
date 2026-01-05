from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('exam/', views.exam_view, name='exam'),
    path('exam/result/', views.result_view, name='result'),
    path('logout/', views.logout_view, name='logout'),
    
]
