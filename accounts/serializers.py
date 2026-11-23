
from rest_framework import serializers

from accounts.models import User,TrainerProfile,StudentProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields =["id","username","password","email","phone","role"]


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model =StudentProfile

        fields ="__all__"

        read_only_fields = ["id","student"]


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:

        model =TrainerProfile

        fields ="__all__"

        read_only_fields = ["id","trainer"]

