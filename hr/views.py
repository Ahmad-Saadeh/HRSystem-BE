import os
from rest_framework import permissions
from rest_framework.parsers import  MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Candidate,Department,Department
from .serializers import CandidateSerializer,DepartmentSerializer,ResumeSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage

# Create your views here.

class CandidateList(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    def list(self, request, *args, **kwargs):
        is_admin = False
        # Check if the request contains the "X-ADMIN" header with a value of "1"
        if request.META.get('HTTP_X_ADMIN') == '1':
            is_admin = True
        # Only return candidates if the user is an admin
        if is_admin:
            candidates = Candidate.objects.all().order_by("-created_at")
            serializer = self.serializer_class(candidates, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response({"detail": "Unauthorized"}, status=401)


class CandidateDetail(APIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser,FormParser]
    def post(self, request):
        data = request.data
        full_name = data.get("full_name")
        date_of_birth = data.get("date_of_birth")
        department_id = data.get("department")
        print("AAAAAAAAAAAa",data)
        try:
            department_instance = Department.objects.get(id=int(department_id))
        except ObjectDoesNotExist:
            return Response({"error": "Department does not exist"}, status=400)
        years_of_experience = data.get("years_of_experience")
        resume_file = request.FILES.get("resume")
        if os.path.splitext(resume_file.name)[1] not in ['.docx','pdf']:
            return Response({"error": "wrong file extention"}, status=400) 
        if resume_file:
            fs = FileSystemStorage()
            fs.save("./resumes/"+resume_file.name, resume_file)
        candidate = Candidate.objects.create(
            full_name=full_name,
            date_of_birth=date_of_birth,
            department=department_instance,
            years_of_experience=years_of_experience,
            resume=resume_file
        )
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data, status=201)


class DepartmentList(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    def get(self, request, *args, **kwargs):
        departments = Department.objects.all()
        serializer = self.serializer_class(departments, many=True)
        return Response(serializer.data, status=200)
    

class ResumeView(RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer_class = ResumeSerializer
    lookup_field = 'pk'
    def retrieve(self, request, *args, **kwargs):
        is_admin = False
        # Check if the request contains the "X-ADMIN" header with a value of "1"
        if request.META.get('HTTP_X_ADMIN') == '1':
            is_admin = True
        # Only return candidates if the user is an admin
        if is_admin:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data['resume'])
        else:
            return Response({"detail": "Unauthorized"}, status=401)