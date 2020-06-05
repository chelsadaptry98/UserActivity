from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,ActivityPeriod
from .serializers import UserSerializer,ActivityPeriodSerializer


class UserList(APIView):

    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)

