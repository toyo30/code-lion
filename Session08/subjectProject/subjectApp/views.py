from django.shortcuts import render, redirect
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm 
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

# class EditSubjectView(UpdateView):
#     model = Subject
#     form_class = SubjectModelForm
#     template_name = 'editSubject.html'
#     success_url = reverse_lazy('home')



def koreanSubjectView(request):
    subjects = Subject.objects.all()
    koreanMajor = subjects.filter(major_name = '국어국문학과')
    return render(request, 'korean.html', {
        'koreanMajor': koreanMajor,
    })

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'home.html', {
        'majors':majors,
        'subjects':subjects,
        })
