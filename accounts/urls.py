from django.urls import path

from accounts.views import TrainerRegisterView,studentRegisterView
from accounts.views import TRainerUpdatedView,TrainerDeatilsView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    #route trainer and student register 
    path("register/trainer/",TrainerRegisterView.as_view()),
    path("register/student/",studentRegisterView.as_view()),

    #route token for trainer
    path("token/trainer/",ObtainAuthToken.as_view()),

    #route trainer details and updated
    path("profile/detail/",TrainerDeatilsView.as_view()),
    path("profile/update/",TRainerUpdatedView.as_view()),

]