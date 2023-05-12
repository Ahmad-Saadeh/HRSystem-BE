from django.contrib import admin
from .models import Department,Candidate

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','date_of_birth','years_of_experience','department','resume','created_at')

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Candidate,CandidateAdmin)