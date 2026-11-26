from django.urls import path ,include

from course_app.views import CourseListView,CourseCreateView,CourseRetrieveUpdateDeleteView

urlpatterns = [

    path("all/",CourseListView.as_view()),
    path("add/",CourseCreateView.as_view()),
    path("edit/<int:pk>/",CourseRetrieveUpdateDeleteView.as_view()),
]