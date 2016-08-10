from django import forms

from .models import Student, Project

# class StudentForm(forms.ModelForm):

class CreateProjectForm(forms.ModelForm):

    students = forms.ModelMultipleChoiceField(\
            queryset=Student.objects.all().filter(project=None),\
            widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Project
        fields = '__all__'

class AssignProjectForm(forms.Form):
    def __init__(self, project=None, *args, **kwargs):
        self.project = kwargs.pop('project', None)
        super(AssignProjectForm, self).__init__(*args, **kwargs)
        self.fields['students'] = forms.ModelMultipleChoiceField(\
                queryset=Student.objects.all().filter(project=self.project),\
                widget=forms.CheckboxSelectMultiple())

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=78)
    message = forms.CharField(max_length=8096, widget=forms.Textarea)
