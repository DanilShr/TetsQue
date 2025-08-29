from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import QuestionViewSet, AnswerViewSet, QuestionListView, QuestionDetailView, \
    AnswerCreateView, AnswerDetailView

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path("api/", include(router.urls)),

    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),

    path('questions/<int:pk>/answers/', AnswerCreateView.as_view(), name='answer-create'),
    path('answers/<int:pk>/', AnswerDetailView.as_view(), name='answer-detail'),

]
