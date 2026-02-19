from rest_framework import serializers
from projects_app.models import Project
from contact_app.models import ContactMessage

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'description', 'tech_stack', 'github_link', 'live_demo_link', 'created_date', 'image']
        read_only_fields = ['slug', 'created_date']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'timestamp']
        read_only_fields = ['timestamp']
