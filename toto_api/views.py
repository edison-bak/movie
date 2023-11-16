from toto.models import Question
from toto_api.serializers import QuestionSerializer
from rest_framework import status

from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth.models import User
from toto_api.serializers import UserSerializer
from rest_framework import generics

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class QuestionList(APIView):
#     def get(self,request):
#         questions = Question.objects.all()
#         # many = True 어려개 있다.
#         serializer = QuestionSerializer(questions, many = True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         # 위와 달리 새로만들어 인스턴스 주지않는다.
#         serializer = QuestionSerializer(data=request.data)
#         # 값이 유효할때만 저장
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class QuestionDetail(APIView):
#     def get(self,request,id):
#         question = get_object_or_404(Question, pk=id)
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)

#     def post(self,request,id):
#         question = get_object_or_404(Question, pk=id)
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:    
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         question = get_object_or_404(Question, pk=id)
#         question.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)