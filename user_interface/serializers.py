from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import (User, InformationModel, EducationModel, ExperienceModel, ProjectModel, MessageModel, SkillsetModel)


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        

class informationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationModel
        fields = "__all__"


class educationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = "__all__"


class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = "__all__"


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = "__all__"


class skillsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsetModel
        fields = "__all__"


class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = "__all__"