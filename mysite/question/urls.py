from django.urls import path
from .views import QuestionView


urlpatterns = [
    path("questions/", QuestionView.as_view(), name="question-list"),
    path("questions/<int:pk>/", QuestionView.as_view(), name="question-detail"),
]
