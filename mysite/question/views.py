
from rest_framework.generics import get_object_or_404

from django.http import JsonResponse

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import QuestionSerializer, AnswerSerializer

from .models import Answer, Question


# Create your views here.
class QuestionView(APIView):
   @swagger_auto_schema(
       operation_description="Запрос всех вопросов (Question)",
       responses={200: QuestionSerializer(many=True)},
   )
   def get(self, request, **kwargs):
       pk = kwargs.get('pk')
       if pk:
           queryset = (Question.objects
                       .prefetch_related('answer').get(pk=pk))
           serializer = QuestionSerializer(queryset)
           return JsonResponse(serializer.data, status=200)
       else:
           queryset = (Question.objects
                       .prefetch_related('answer').all())
           serialized_data = QuestionSerializer(queryset, many=True)
           return JsonResponse(serialized_data.data, safe=False)

   @swagger_auto_schema(
       request_body=QuestionSerializer,
       responses={200: QuestionSerializer()},
   )
   def post(self, request):
       serialized_data = QuestionSerializer(data=request.POST)
       if serialized_data.is_valid():
           serialized_data.save()
           return JsonResponse(serialized_data.data, safe=False)
       else:
           return JsonResponse(serialized_data.errors, safe=False)

   def delete(self, request, **kwargs):
       pk = kwargs['pk']
       queryset = Question.objects.get(pk=pk)
       return JsonResponse({"Удалена запись":"ok"}, status=204)


class AnswerView(APIView):
    @swagger_auto_schema(
        responses={200: AnswerSerializer()},
    )
    def get(self, request, **kwargs):
        user = request.user
        pk = kwargs.get('pk')
        queryset = get_object_or_404(Answer.objects.select_related('user', 'question'), pk=pk)
        serialized_data = AnswerSerializer(queryset)
        return JsonResponse(serialized_data.data)

    @swagger_auto_schema(
        request_body=AnswerSerializer,
        responses={200: AnswerSerializer()},
    )
    def post(self, request, **kwargs):
        pk_q = kwargs.get('pk')
        question = Question.objects.get(pk=pk_q)
        if question:
            data = request.data
            print(data)
            data['question'] = pk_q
            serialized_data = AnswerSerializer(data=data)
            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse(serialized_data.data, safe=False)
            else:
                return JsonResponse(serialized_data.errors, safe=False)
        else:
            return Response(status=404)


    def delete(self, request, **kwargs):
        pk = kwargs.get('pk')
        answer = get_object_or_404(Answer, pk=pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











