from django.test import TestCase
from rest_framework.test import APITestCase
from datetime import date, datetime, timedelta,timezone
from .models import Department, Candidate
from rest_framework import status
from .serializers import CandidateSerializer, DepartmentSerializer
from rest_framework.test import APIClient
from django.urls import reverse

# Create your tests here.

# models

class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='IT')

    def test_department_name(self):
        self.assertEqual(self.department.name, 'IT')

    def test_department_str_representation(self):
        self.assertEqual(str(self.department), 'IT')

class CandidateModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='IT')
        self.candidate = Candidate.objects.create(
            full_name='Ahmad Saadeh',
            date_of_birth=date(1996, 6, 16),
            years_of_experience=4,
            department=self.department,
            resume='resumes/Ahmads_Resume.pdf',
            created_at=None
        )

    def test_candidate_full_name(self):
        self.assertEqual(self.candidate.full_name, 'Ahmad Saadeh')

    def test_candidate_date_of_birth(self):
        self.assertEqual(self.candidate.date_of_birth, date(1996, 6, 16))

    def test_candidate_years_of_experience(self):
        self.assertEqual(self.candidate.years_of_experience, 4)

    def test_candidate_department(self):
        self.assertEqual(self.candidate.department, self.department)

    def test_candidate_resume(self):
        self.assertEqual(self.candidate.resume, 'resumes/Ahmads_Resume.pdf')

    def test_candidate_created_at(self):
        now = datetime.now(timezone.utc)
        created_at_aware = self.candidate.created_at.replace(tzinfo=timezone.utc)
        difference = timedelta(seconds=1)
        self.assertLessEqual(created_at_aware, now)
        self.assertGreaterEqual(created_at_aware, now - difference)


# views


class CandidateListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name='IT')
        self.candidate = Candidate.objects.create(
            full_name='Ahmad Saadeh',
            date_of_birth='1996-06-16',
            years_of_experience=4,
            department=self.department,
            resume='resumes/Ahmads_Resume.pdf'
        )

    def test_get_candidate_list(self):
        response = self.client.get('/api/candidate-list/',HTTP_X_ADMIN='1')  # Update the URL here
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class CandidateDetailTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name='IT')

    def test_create_candidate(self):
        url = reverse('candidate-details')
        data = {
            "full_name": "Ahmad Saadeh",
            "date_of_birth": "1996-06-16",
            "department": 1,
            "years_of_experience": 4,
            "resume": open('resumes/Ahmads_Resume.pdf', 'rb')
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidate.objects.count(), 1)
        candidate = Candidate.objects.first()
        self.assertEqual(candidate.full_name, "Ahmad Saadeh")
        self.assertEqual(candidate.date_of_birth, date(1996, 6, 16))
        self.assertEqual(candidate.department_id, 1)
        self.assertEqual(candidate.years_of_experience, 4)
        expected_serializer_data = CandidateSerializer(candidate).data
        self.assertEqual(response.data, expected_serializer_data)

class DepartmentListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name='IT')

    def test_get_department_list(self):
        response = self.client.get('/api/departments-list/')  # Update the URL here
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class ResumeViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name='IT')
        self.candidate = Candidate.objects.create(
            full_name='Ahmad Saadeh',
            date_of_birth='1996-06-16',
            years_of_experience=4,
            department=self.department,
            resume='resumes/Ahmads_Resume.pdf',
        )

    def test_get_resume(self):
        response = self.client.get(f'/api/get-resume/{self.candidate.id}/',HTTP_X_ADMIN='1')  # Update the URL here
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
