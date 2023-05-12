from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Candidate(models.Model):
 
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    years_of_experience = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)