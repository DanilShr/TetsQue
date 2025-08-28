from django.db.models.expressions import result
from django.http import JsonResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import QuestionSerializer

from .models import Answer, Question


# Create your views here.
class QuestionView(APIView):
   @swagger_auto_schema(
       responses={200: QuestionSerializer(many=True)},
   )
   def get(self, request, **kwargs):
       pk = kwargs.get('pk')
       if pk:
           queryset = (Question.objects
                       .prefetch_related('answers').get(pk=pk))
           serializer = QuestionSerializer(queryset)
           return JsonResponse(serializer.data, status=200)
       else:
           queryset = (Question.objects
                       .prefetch_related('answers').all())
           print(queryset)
           serialized_data = QuestionSerializer(queryset, many=True)
           print(serialized_data.data)
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
       result, id = queryset.delete()
       return JsonResponse({"Удалена запись":"ok"}, status=204)







