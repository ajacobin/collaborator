from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse_lazy

from django.core.mail import send_mail

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, FormView


from .models import Student, Project
from .forms import CreateProjectForm, AssignProjectForm, EmailForm

import code

class StudentCreateView(CreateView):
    model = Student
    fields = ['fname','lname','email','position','action']
    template_name = "StudentCreate.html"

class StudentDetailView(DetailView):
    model = Student
    template_name = "StudentDetail.html"

class StudentListView(LoginRequiredMixin, ListView):
    login_url = '/admin/'
    redirect_field_name = '/sami-dash'
    model = Project
    template_name = "StudentList.html"


class ProjectDetailView(LoginRequiredMixin, FormView, DetailView):
    login_url = '/admin/'
    redirect_field_name = '/sami-dash'
    model = Project
    template_name = "ProjectDetail.html"
    form_class = AssignProjectForm

    def get_form_kwargs(self):
        kwargs = super(ProjectDetailView, self).get_form_kwargs()
        self.kwargs['project'] = Project.objects.get(pk=self.kwargs['pk'])
        # code.interact(local=dict(globals(), **locals()))
        return kwargs

class ProjectListView(LoginRequiredMixin, ListView):
    login_url = '/admin/'
    redirect_field_name = '/sami-dash'
    model = Project
    queryset = Project.objects.all()
    template_name = "ProjectList.html"


class SamiDashboardView(LoginRequiredMixin, FormView, TemplateView):
    login_url = '/admin/'
    redirect_field_name = '/sami-dash'
    template_name = "SamiDash.html"
    form_class = CreateProjectForm

    def get_context_data(self, **kwargs):
        context = super(SamiDashboardView, self).get_context_data(**kwargs)
        context['students'] = Student.objects.all().filter(project=None)
        context['projects'] = Project.objects.all()
        return context

def ProjectCreate(request, **kwargs):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            new_project = Project(name=form.data['name'], description=form.data['description'])
            new_project.save()
            for student in form.cleaned_data['students']:
                student.project = new_project
                student.save()
                # code.interact(local=dict(globals(), **locals()))
    return redirect(reverse_lazy('sami-dash'))

def ProjectAssign(request, **kwargs):
    if request.method == "POST":
        form = AssignProjectForm(request.POST)
        if form.is_valid():
            code.interact(local=dict(globals(), **locals()))
    return

def EmailMessage(request, **kwargs):
    if request.method == "GET":
        project = Project.objects.get(pk=kwargs['pk'])
        form = EmailForm()
        # code.interact(local=dict(globals(), **locals()))
        return render(request, 'EmailProject.html', {'project':project, 'form':form})
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            project = Project.objects.get(pk=kwargs['pk'])
            email = []
            for student in project.students.all():
                email.append(student.email)

            # code.interact(local=dict(globals(), **locals()))
            try:
                send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    'collab-admin@collab-machine.loc',
                    email,
                    fail_silently=False)
            except Exception as e:
                return HttpResponse("Error:%s" % e)
    return redirect('project-detail', pk=kwargs['pk'])
