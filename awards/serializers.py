from rest_framework import serializers
from .models import Project, Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_title', 'project_description', 'project_screenshot','project_link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','phone_number')