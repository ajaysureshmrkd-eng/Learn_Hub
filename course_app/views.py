from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions

from accounts.permissions import Istrainer

from course_app.models import Course
from course_app.serializers import CourseSerialiazer
# Create your views here.


class CourseListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [Istrainer]

    serializer_class = CourseSerialiazer

    queryset = Course.objects.all()


class CourseCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [Istrainer]

    serializer_class = CourseSerialiazer

    queryset = Course.objects.all()

    def perform_create(self,serializer):

        serializer.save(trainer=self.request.user)

class CourseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [Istrainer]

    serializer_class = CourseSerialiazer

    queryset = Course.objects.all()

