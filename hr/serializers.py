from rest_framework.serializers import ModelSerializer
from .models import Department, Candidate


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['full_name', 'date_of_birth', 'years_of_experience', 'department','resume']

class ResumeSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','resume',]
        