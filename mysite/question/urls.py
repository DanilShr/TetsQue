from django.urls import path
from .views import QuestionView, AnswerView

urlpatterns = [
    path("questions/", QuestionView.as_view(), name="question-list"),
    path("questions/<int:pk>/", QuestionView.as_view(), name="question-detail"),
    path('answers/<int:pk>/', AnswerView.as_view(), name="answer-detail"),
    path('questions/<int:pk>/answers/', AnswerView.as_view(), name="answer-list"),

]
