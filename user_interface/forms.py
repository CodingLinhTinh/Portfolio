from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import (User, InformationModel, EducationModel, ExperienceModel, ProjectModel, MessageModel, SkillsetModel)

class IntroForm(ModelForm):
    class Meta:
        model = InformationModel
        fields= "__all__"
    
    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.__contains__('request'):
            request = kwargs.pop('request')
        m = super(IntroForm, self).save(commit=False, *args, **kwargs)
        if m.user is None and request is not None:
            m.user = request.user
            m.save()

class  EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = ["title", "the_year", "institute", "description"]
        labels = {'title': 'Level of Education', 'the_year': "Year", 'institute': "Institute" }
    
    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.__contains__('request'):
            request = kwargs.pop('request')
        m = super(EducationForm, self).save(commit=False, *args, **kwargs)
        if m.user is None and request is not None:
            m.user = request.user
            m.save()


class  ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = ["title", "the_year", "institute", "description"]
        labels = {'title': 'Position', 'the_year': "Year", 'institute': "Company Name" }

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.__contains__('request'):
            request = kwargs.pop('request')
        m = super(ExperienceForm, self).save(commit=False, *args, **kwargs)
        if m.user is None and request is not None:
            m.user = request.user
            m.save()

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectModel
        #fields= "__all__" 
        exclude = ('user', )

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.__contains__('request'):
            request = kwargs.pop('request')
        m = super(ProjectForm, self).save(commit=False, *args, **kwargs)
        if m.user is None and request is not None:
            m.user = request.user
            m.save()


class SkillsetForm(ModelForm):
    class Meta:
        model = SkillsetModel
        #fields= "__all__" 
        exclude = ('user', )

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.__contains__('request'):
            request = kwargs.pop('request')
        m = super(SkillsetForm, self).save(commit=False, *args, **kwargs)
        if m.user is None and request is not None:
            m.user = request.user
            m.save()

class MessageForm(ModelForm):
    class Meta:
        model = MessageModel
        fields=['name', 'email', 'message', 'subject']

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.__contains__('request'):
            request = kwargs.pop('request')
        m = super(MessageForm, self).save(commit=False, *args, **kwargs)
        if m.user is None and request is not None:
            m.user = request.user
            m.save()

class ContactForm(forms.Form):
    name = forms.CharField(max_length= 50)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
    subject = forms.CharField(widget=forms.Textarea, max_length=2000)

