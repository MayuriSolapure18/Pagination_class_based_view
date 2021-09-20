from django.shortcuts import render
from django.views.generic import ListView

from .models import Student
# Create your views here.

class Studentlist(ListView):
    queryset = Student.objects.all()
    template_name = 'Student_list.html'
    paginate_by = 3