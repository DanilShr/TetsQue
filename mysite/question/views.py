from rest_framework.generics import get_object_or_404

from django.http import JsonResponse

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import QuestionSerializer, AnswerSerializer

from .models import Answer, Question


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    include_in_schema = False


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    include_in_schema = False


# Create your views here.
class QuestionListView(APIView):
    """Вопросы - список и создание"""

    @swagger_auto_schema(
        operation_description="Получить список всех вопросов",
        responses={200: QuestionSerializer(many=True)},
    )
    def get(self, request):
        queryset = Question.objects.prefetch_related("answer").all()
        serialized_data = QuestionSerializer(queryset, many=True)
        return JsonResponse(serialized_data.data, safe=False)

    @swagger_auto_schema(
        operation_description="Создать новый вопрос",
        request_body=QuestionSerializer,
        responses={201: QuestionSerializer()},
    )
    def post(self, request):
        serialized_data = QuestionSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data, status=201)
        return JsonResponse(serialized_data.errors, status=400)


class QuestionDetailView(APIView):
    """Вопрос - детали, удаление"""

    @swagger_auto_schema(
        operation_description="Получить вопрос и все ответы на него",
        responses={200: QuestionSerializer()},
    )
    def get(self, request, pk):
        question = get_object_or_404(Question.objects.prefetch_related("answer"), pk=pk)
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Удалить вопрос (вместе с ответами)",
        responses={204: "No content"},
    )
    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return JsonResponse({"Удалена запись": "ok"}, status=204)


class AnswerCreateView(APIView):
    """Создание ответа к вопросу"""

    @swagger_auto_schema(
        operation_description="Добавить ответ к вопросу",
        request_body=AnswerSerializer,
        responses={201: AnswerSerializer()},
    )
    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        data = request.data.copy()
        data["question"] = pk
        serialized_data = AnswerSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data, status=201)
        return JsonResponse(serialized_data.errors, status=400)


class AnswerDetailView(APIView):
    """Ответ - детали, удаление"""

    @swagger_auto_schema(
        operation_description="Получить конкретный ответ",
        responses={200: AnswerSerializer()},
    )
    def get(self, request, pk):
        answer = get_object_or_404(
            Answer.objects.select_related("user", "question"), pk=pk
        )
        serialized_data = AnswerSerializer(answer)
        return JsonResponse(serialized_data.data)

    @swagger_auto_schema(
        operation_description="Удалить ответ",
        responses={204: "No content"},
    )
    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
