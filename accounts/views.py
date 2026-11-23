from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from accounts.models import User,TrainerProfile
from accounts.serializers import UserSerializer,TrainerSerializer
from accounts.permissions import Istrainer




class TrainerRegisterView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data =serializer.validated_data

            instance = User.objects.create_superuser(role="trainer",**cleaned_data)

            serializer = UserSerializer(instance)

            return Response(data=serializer.data)

        else:

            return Response (data=serializer.errors)

class studentRegisterView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data =serializer.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer = UserSerializer(instance)

            return Response(data=serializer.data)

        else:

            return Response (data=serializer.errors)


class TrainerDeatilsView(APIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated,Istrainer]

    def get(self,request):

        instance = request.user.trainer

        seriliazer = TrainerSerializer(instance)

        return Response (data=seriliazer.data)

class TRainerUpdatedView(APIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated,Istrainer]


    def put(self,request,pk=None):

        form_data = request.data

        instance = request.user.trainer

        seriliazer = TrainerSerializer(data=form_data,instance=instance)

        if seriliazer.is_valid():

            seriliazer.save()

            return Response (data=seriliazer.data)

        else:

            return Response (data=seriliazer.errors)
    