from .models import Company, Job
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "job_title", "job_description", "date_posted", "category"]
