from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# your_app_name/views.py



def student_registration_form(request):
    """Renders the student registration form HTML page."""
    return render(request, 'index.html')
