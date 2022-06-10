from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from .models import (User, InformationModel, EducationModel, ExperienceModel, ProjectModel, MessageModel, SkillsetModel)
from .forms import (IntroForm, EducationForm, ExperienceForm, MessageForm, SkillsetForm, ProjectForm, ContactForm)
from django.core.mail import send_mail, BadHeaderError
from .serializers import (userSerializer, informationSerializer, educationSerializer, experienceSerializer, projectSerializer, skillsetSerializer, messageSerializer)
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import serializers, permissions
# Create your views here.

def index(request):
    return render(request, template_name="user_interface/index.html")
    # return HttpResponse("Hello, world. You're at the polls index.")

#Create, Retrieve, Update, Delete ----> CRUD
@login_required(login_url='login')
def form_createView(request, *args, **kwargs):
    template_name = 'user_interface/create.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"

    intro_form = IntroForm(request.POST or None)
    if intro_form.is_valid():
        intro_form.save(commit = False)
        intro_form.user = user
        intro_form.save(request = request)
    else:
        intro_form = IntroForm()

    edu_form = EducationForm(request.POST or None)
    if edu_form.is_valid():
        edu_form.save(commit=False)
        edu_form.user = user
        edu_form.save(request = request)
    else:
        edu_form = EducationForm()

    exp_form = ExperienceForm(request.POST or None)
    if exp_form.is_valid():
        exp_form.save(commit=False)
        exp_form.user = user
        exp_form.save(request = request)
    else:
        exp_form = ExperienceForm()

    project_form = ProjectForm(request.POST or None)
    if project_form.is_valid():
        project_form.save(commit=False)
        project_form.user = user
        project_form.save(request = request)
    else:
        project_form = ProjectForm()
    
    skill_form = SkillsetForm(request.POST or None)
    if skill_form.is_valid():
        skill_form.save(commit=False)
        skill_form.user = user
        skill_form.save(request = request)
    else:
        skill_form = SkillsetForm()

    context = {
        'user': user,
        'introFORM': IntroForm(),
        'eduFORM': EducationForm(),
        'expFORM': ExperienceForm(),
        'projectFORM': ProjectForm(),
        'skillFORM': SkillsetForm(), # skill_form,
    }

    return render(request, template_name, context)

#Information form view
@login_required(login_url='login')
def introForm_createView(request, *args, **kwargs):
    template_name = 'user_interface/information_create.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    if request.method == 'POST':
        intro_form = IntroForm(request.POST or None)
        if intro_form.is_valid():
            intro_form.save(commit = False)
            intro_form.user = user
            intro_form.save(request = request)
    else:
        intro_form = IntroForm()
    context = {
        'user': user,
        'introFORM': IntroForm(),
    }
    return render(request, template_name, context)

#Education form view
@login_required(login_url='login')
def eduForm_createView(request, *args, **kwargs):
    template_name = 'user_interface/education_create.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    bioProfile = User.objects.get(username = user)
    education_qs = EducationModel.objects.filter(user = bioProfile).all()
    education_serializer = educationSerializer(education_qs, many=True)

    if request.method == 'POST':
        edu_form = EducationForm(request.POST or None)
        if edu_form.is_valid():
            edu_form.save(commit=False)
            edu_form.user = user
            edu_form.save(request = request)
    else:
        edu_form = EducationForm()
    context = {
        'user': user,
        'eduFORM': EducationForm(),
        "education": education_serializer.data,
    }
    return render(request, template_name, context)

#Experiece form view
@login_required(login_url='login')
def expForm_createView(request, *args, **kwargs):
    template_name = 'user_interface/experience_create.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    bioProfile = User.objects.get(username = user)
    experience_qs = ExperienceModel.objects.filter(user = bioProfile).all()
    experience_serializer = experienceSerializer(experience_qs, many=True)
    if request.method == 'POST':
        exp_form = ExperienceForm(request.POST or None)
        if exp_form.is_valid():
            exp_form.save(commit=False)
            exp_form.user = user
            exp_form.save(request = request)
    else:
        exp_form = ExperienceForm()
    context = {
        'user': user,
        'expFORM': ExperienceForm(),
        "experience": experience_serializer.data,
    }
    return render(request, template_name, context)

#Project form view
@login_required(login_url='login')
def projectForm_createView(request, *args, **kwargs):
    template_name = 'user_interface/project_create.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    bioProfile = User.objects.get(username = user)
    project_qs = ProjectModel.objects.filter(user = bioProfile).all()
    project_serializer = projectSerializer(project_qs, many=True)
    if request.method == 'POST':
        project_form = ProjectForm(request.POST or None)
        if project_form.is_valid():
            project_form.save(commit=False)
            project_form.user = user
            project_form.save(request = request)
    else:
        project_form = ProjectForm()
    context = {
        'user': user,
        'projectFORM': ProjectForm(),
        "projects": project_serializer.data,
    }
    return render(request, template_name, context)



#Project form view
@login_required(login_url='login')
def skillForm_createView(request, *args, **kwargs):
    template_name = 'user_interface/skill_create.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    bioProfile = User.objects.get(username = user)
    skillset_qs = SkillsetModel.objects.filter(user = bioProfile).all()
    skillset_serializer = skillsetSerializer(skillset_qs, many=True)

    if request.method == 'POST':
        skill_form = SkillsetForm(request.POST or None)
        if skill_form.is_valid():
            skill_form.save(commit=False)
            skill_form.user = user
            skill_form.save(request = request)
    else:
        skill_form = SkillsetForm()

    context = {
        'user': user,
        'skillFORM': SkillsetForm(), # skill_form,
        "skillsets": skillset_serializer.data,
    }
    return render(request, template_name, context)



@api_view(['GET'])
@permission_classes((permissions.AllowAny, permissions.IsAuthenticated))
def api_view(request, username, *args, **kwargs):
    bioProfile = User.objects.get(username = username)
    information_qs = InformationModel.objects.filter(user = bioProfile).first()
    education_qs = EducationModel.objects.filter(user = bioProfile).all()
    experience_qs = ExperienceModel.objects.filter(user = bioProfile).all()
    project_qs = ProjectModel.objects.filter(user = bioProfile).all()
    skillset_qs = SkillsetModel.objects.filter(user = bioProfile).all()
    message_qs = MessageModel.objects.filter(user = bioProfile).all()
    messageform_qs = MessageForm()
    #Calling Serializers
    username_serializer = userSerializer(bioProfile, many=False)
    information_serializer = informationSerializer(information_qs, many=False)
    education_serializer = educationSerializer(education_qs, many=True)
    experience_serializer = experienceSerializer(experience_qs, many=True)
    project_serializer = projectSerializer(project_qs, many=True)
    skillset_serializer = skillsetSerializer(skillset_qs, many=True)
    message_serializer = messageSerializer(message_qs, many=True)
    context = {
        "username": username,
        "user": username_serializer.data,
        "information": information_serializer.data,
        "education": education_serializer.data,
        "experience": experience_serializer.data,
        "projects": project_serializer.data,
        "skillsets": skillset_serializer.data,
        # "message_form": messageform_qs.data,
    }
    return Response(context)



def portfolio_view(request, username, *args, **kwargs):
    template_name = 'user_interface/portfolio.html'
    context = {}
    userprofile = get_object_or_404(User, username = username)

    # try:
    #     userprofile = User.objects.get(username = username)
    # except User.DoesNotExist:
    #     raise Http404('User does not exists.  Please provide user information first')

    bioProfile = User.objects.get(username = username)
    information_qs = InformationModel.objects.filter(user = bioProfile).first()
    education_qs = EducationModel.objects.filter(user = bioProfile).all()
    experience_qs = ExperienceModel.objects.filter(user = bioProfile).all()
    project_qs = ProjectModel.objects.filter(user = bioProfile).all()
    skillset_qs = SkillsetModel.objects.filter(user = bioProfile).all()
    message_qs = MessageModel.objects.filter(user = bioProfile).all()
    messageform_qs = MessageForm()
    #Calling Serializers
    username_serializer = userSerializer(bioProfile, many=False)
    information_serializer = informationSerializer(information_qs, many=False)
    education_serializer = educationSerializer(education_qs, many=True)
    experience_serializer = experienceSerializer(experience_qs, many=True)
    project_serializer = projectSerializer(project_qs, many=True)
    skillset_serializer = skillsetSerializer(skillset_qs, many=True)
    message_serializer = messageSerializer(message_qs, many=True)

    if request.method == "GET":
        print('GET METHOD WORKING')
        form = ContactForm()
        context = {
        "username": username,
        "user": username_serializer.data,
        "information": information_serializer.data,
        "education": education_serializer.data,
        "experience": experience_serializer.data,
        "projects": project_serializer.data,
        "skillsets": skillset_serializer.data,
        # "message_form": messageform_qs.data,
        "form": form.data,
    }

    else:
        print('POST METHOD BEING CALLED')
        to_email = information_qs.email
        print(f'To EMAIL of portfolio user. ---> {to_email}')
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            new_subject = 'SENDER: ' + name + ' SUBJECT:' + subject
            # print(name, from_email, new_subject, message)
            try:
                send_mail(new_subject, message, from_email, [to_email, 'admin@mail.com'])
                form_message = "Thank You for cennecting with us. Your message has been received!" 
            except BadHeaderError:
                form_message = "There was bad header error. Please try again" 
                # return HttpResponseRedirect(reverse("portfolio"))
                return redirect('portfolio')
        # COntact form works
        context = {
            "username": username,
            "user": username_serializer.data,
            "information": information_serializer.data,
            "education": education_serializer.data,
            "experience": experience_serializer.data,
            "projects": project_serializer.data,
            "skillsets": skillset_serializer.data,
            # "message_form": messageform_qs.data,
            "form": form,
            "form_message": form_message,
        }
    
    return render(request, template_name, context)


# ---------------- UPDATE VIEW WORKS
@login_required(login_url='login')
def introForm_updateView(request, *args, **kwargs):
    template_name = 'user_interface/update/information_update.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    try:
        obj = InformationModel.objects.filter(user = user).first()
    except:
        raise Http404
    bioProfile = User.objects.get(username = user)
    information_qs = InformationModel.objects.filter(user = bioProfile).first()
    education_qs = EducationModel.objects.filter(user = bioProfile).all()
    experience_qs = ExperienceModel.objects.filter(user = bioProfile).all()
    project_qs = ProjectModel.objects.filter(user = bioProfile).all()
    skillset_qs = SkillsetModel.objects.filter(user = bioProfile).all()
    list_project_id = []
    list_exp_id = []
    list_edu_id = []
    list_skill_id =[]
    # list_information_id= []
    # for information in information_qs:
    #     list_information_id.append(information.id)
    for project in project_qs:
        list_project_id.append(project.id)
    for exp in experience_qs:
        list_exp_id.append(exp.id)
    for edu in education_qs:
        list_edu_id.append(edu.id)
    for skill in skillset_qs:
        list_skill_id.append(skill.id)
    if request.method == 'POST':
        intro_form = IntroForm(request.POST or None, instance = obj)
        if intro_form.is_valid():
            intro_form.save(commit = False)
            intro_form.user = user
            intro_form.save(request = request)
    else:
        intro_form = IntroForm(instance = obj)
    context = {
        'user': user,
        'current_information_id': information_qs.id,
        'first_edu_id': list_edu_id[0],
        'first_exp_id': list_exp_id[0],
        'first_project_id': list_project_id[0],
        'first_skill_id':list_skill_id[0],
        'introFORM': intro_form,
    }
    return render(request, template_name, context)
    
#Education form view
@login_required(login_url='login')
def eduForm_updateView(request, id, *args, **kwargs):
    template_name = 'user_interface/update/education_update.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    bioProfile = User.objects.get(username = user)
    education_qs = EducationModel.objects.filter(user = bioProfile).all()
    experience_qs = ExperienceModel.objects.filter(user = bioProfile).all()
    project_qs = ProjectModel.objects.filter(user = bioProfile).all()
    skillset_qs = SkillsetModel.objects.filter(user = bioProfile).all()
    education_serializer = educationSerializer(education_qs, many=True)
    next_id = id + 1
    previous_id = id - 1

    try:
        obj = EducationModel.objects.get(user = user, pk = id)
    except:
        raise Http404
    list_project_id = []
    list_exp_id = []
    list_edu_id = []
    list_skill_id =[]
    for project in project_qs:
        list_project_id.append(project.id)
    for exp in experience_qs:
        list_exp_id.append(exp.id)
    for edu in education_qs:
        list_edu_id.append(edu.id)
    for skill in skillset_qs:
        list_skill_id.append(skill.id)
    # print(f'Id list of educaiton qs: {list_id}')

    if request.method == 'POST':
        edu_form = EducationForm(request.POST or None, instance=obj)
        if edu_form.is_valid():
            edu_form.save(commit=False)
            edu_form.user = user
            edu_form.save(request = request)
    else:
        edu_form = EducationForm(instance=obj)
    context = {
        'user': user,
        "current_id":id,
        'first_edu_id': list_edu_id[0],
        'first_exp_id': list_exp_id[0],
        'first_project_id': list_project_id[0],
        'first_skill_id':list_skill_id[0],
        "next_id": next_id,
        "previous_id": previous_id,
        'eduFORM': edu_form,
        "education": education_serializer.data,
    }
    return render(request, template_name, context)

#Experiece form view
@login_required(login_url='login')
def expForm_updateView(request, id,  *args, **kwargs):
    template_name = 'user_interface/update/experience_update.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    bioProfile = User.objects.get(username = user)
    experience_qs = ExperienceModel.objects.filter(user = bioProfile).all()
    education_qs = EducationModel.objects.filter(user = bioProfile).all()
    project_qs = ProjectModel.objects.filter(user = bioProfile).all()
    skillset_qs = SkillsetModel.objects.filter(user = bioProfile).all()
    experience_serializer = experienceSerializer(experience_qs, many=True)
    obj = get_object_or_404(ExperienceModel, user = user, pk=id)
    list_project_id = []
    list_exp_id = []
    list_edu_id = []
    list_skill_id =[]
    for project in project_qs:
        list_project_id.append(project.id)
    for exp in experience_qs:
        list_exp_id.append(exp.id)
    for edu in education_qs:
        list_edu_id.append(edu.id)
    for skill in skillset_qs:
        list_skill_id.append(skill.id)

    if request.method == 'POST':
        exp_form = ExperienceForm(request.POST or None, instance=obj)
        if exp_form.is_valid():
            exp_form.save(commit=False)
            exp_form.user = user
            exp_form.save(request = request)
    else:
        exp_form = ExperienceForm(instance=obj)
    context = {
        'user': user,
        "current_id":id,
        "previous_id": id-1,
        "next_id": id+1,
        'first_edu_id': list_edu_id[0],
        'first_exp_id': list_exp_id[0],
        'first_project_id': list_project_id[0],
        'first_skill_id':list_skill_id[0],        
        'expFORM': exp_form,
        "experience": experience_serializer.data,
    }
    return render(request, template_name, context)

#Project form view
@login_required(login_url='login')
def projectForm_updateView(request, id, *args, **kwargs):
    template_name = 'user_interface/update/project_update.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    bioProfile = User.objects.get(username = user)
    project_qs = ProjectModel.objects.filter(user = bioProfile).all()
    education_qs = EducationModel.objects.filter(user = bioProfile).all()
    experience_qs = ExperienceModel.objects.filter(user = bioProfile).all()
    skillset_qs = SkillsetModel.objects.filter(user = bioProfile).all()
    project_serializer = projectSerializer(project_qs, many=True)
    obj = get_object_or_404(ProjectModel, user = user, pk=id)

    list_project_id = []
    list_exp_id = []
    list_edu_id = []
    list_skill_id =[]
    for project in project_qs:
        list_project_id.append(project.id)
    for exp in experience_qs:
        list_exp_id.append(exp.id)
    for edu in education_qs:
        list_edu_id.append(edu.id)
    for skill in skillset_qs:
        list_skill_id.append(skill.id)

    if request.method == 'POST':
        project_form = ProjectForm(request.POST or None, instance=obj)
        if project_form.is_valid():
            project_form.save(commit=False)
            project_form.user = user
            project_form.save(request = request)
    else:
        project_form = ProjectForm(instance=obj)
    context = {
        'user': user,
        "current_id":id,
        'first_edu_id': list_edu_id[0],
        'first_exp_id': list_exp_id[0],
        'first_project_id': list_project_id[0],
        'first_skill_id':list_skill_id[0],  
        'next_id': id+1,
        'previous_id': id -1,
        'projectFORM': project_form,
        "projects": project_serializer.data,
    }
    return render(request, template_name, context)



#Project form view
@login_required(login_url='login')
def skillForm_updateView(request, id, *args, **kwargs):
    template_name = 'user_interface/update/skill_update.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    bioProfile = User.objects.get(username = user)
    skillset_qs = SkillsetModel.objects.filter(user = bioProfile).all()
    skillset_serializer = skillsetSerializer(skillset_qs, many=True)
    education_qs = EducationModel.objects.filter(user = bioProfile).all()
    experience_qs = ExperienceModel.objects.filter(user = bioProfile).all()
    project_qs = ProjectModel.objects.filter(user = bioProfile).all()
    obj = get_object_or_404(SkillsetModel, user = user, pk=id)
    list_project_id = []
    list_exp_id = []
    list_edu_id = []
    list_skill_id =[]
    for project in project_qs:
        list_project_id.append(project.id)
    for exp in experience_qs:
        list_exp_id.append(exp.id)
    for edu in education_qs:
        list_edu_id.append(edu.id)
    for skill in skillset_qs:
        list_skill_id.append(skill.id)

    if request.method == 'POST':
        skill_form = SkillsetForm(request.POST or None, instance=obj)
        if skill_form.is_valid():
            skill_form.save(commit=False)
            skill_form.user = user
            skill_form.save(request = request)
    else:
        skill_form = SkillsetForm(instance= obj)

    context = {
        'user': user,
        "current_id":id,
        'first_edu_id': list_edu_id[0],
        'first_exp_id': list_exp_id[0],
        'first_project_id': list_project_id[0],
        'first_skill_id':list_skill_id[0],
        'next_id': id+1,
        'previous_id': id-1,
        'skillFORM': skill_form, # skill_form,
        "skillsets": skillset_serializer.data,
    }
    return render(request, template_name, context)

@login_required(login_url='login')
def information_deleteView(request, id, *args, **kwargs):
    template_name = 'user_interface/delete.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    obj_information = get_object_or_404(InformationModel, user = user, pk=id)
    # obj_education = get_object_or_404(EducationModel, user = user, pk=id)
    # obj_experience = get_object_or_404(ExperienceModel, user = user, pk=id)
    # obj_project = get_object_or_404(ProjectModel, user = user, pk=id)
    # obj_skill = get_object_or_404(SkillsetModel, user = user, pk=id)
    if request.method == 'POST':
        obj_information.delete()
        
    context = {
        'user': user,
        'id': id,
    }
    return render(request, template_name, context)


@login_required(login_url='login')
def education_deleteView(request, id, *args, **kwargs):
    template_name = 'user_interface/delete.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    # obj_information = get_object_or_404(InformationModel, user = user, pk=id)
    obj_education = get_object_or_404(EducationModel, user = user, pk=id)
    # obj_experience = get_object_or_404(ExperienceModel, user = user, pk=id)
    # obj_project = get_object_or_404(ProjectModel, user = user, pk=id)
    # obj_skill = get_object_or_404(SkillsetModel, user = user, pk=id)
    if request.method == 'POST':
        obj_education.delete()
       
    context = {
        'user': user,
        'id': id,
    }
    return render(request, template_name, context)

@login_required(login_url='login')
def experience_deleteView(request, id, *args, **kwargs):
    template_name = 'user_interface/delete.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    # obj_information = get_object_or_404(InformationModel, user = user, pk=id)
    # obj_education = get_object_or_404(EducationModel, user = user, pk=id)
    obj_experience = get_object_or_404(ExperienceModel, user = user, pk=id)
    # obj_project = get_object_or_404(ProjectModel, user = user, pk=id)
    # obj_skill = get_object_or_404(SkillsetModel, user = user, pk=id)
    if request.method == 'POST':
        obj_experience.delete()
    
    context = {
        'user': user,
        'id': id,
    }
    return render(request, template_name, context)

@login_required(login_url='login')
def project_deleteView(request, id, *args, **kwargs):
    template_name = 'user_interface/delete.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    # obj_information = get_object_or_404(InformationModel, user = user, pk=id)
    # obj_education = get_object_or_404(EducationModel, user = user, pk=id)
    # obj_experience = get_object_or_404(ExperienceModel, user = user, pk=id)
    obj_project = get_object_or_404(ProjectModel, user = user, pk=id)
    # obj_skill = get_object_or_404(SkillsetModel, user = user, pk=id)
    if request.method == 'POST':
        obj_project.delete()
    context = {
        'user': user,
        'id': id,
    }
    return render(request, template_name, context)

@login_required(login_url='login')
def skillset_deleteView(request, id, *args, **kwargs):
    template_name = 'user_interface/delete.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"
    # obj_information = get_object_or_404(InformationModel, user = user, pk=id)
    # obj_education = get_object_or_404(EducationModel, user = user, pk=id)
    # obj_experience = get_object_or_404(ExperienceModel, user = user, pk=id)
    # obj_project = get_object_or_404(ProjectModel, user = user, pk=id)
    obj_skill = get_object_or_404(SkillsetModel, user = user, pk=id)
    if request.method == 'POST':
        obj_skill.delete()
    context = {
        'user': user,
        'id': id,
    }
    return render(request, template_name, context)


def login_view(request, *args, **kwargs): 
    if request.method == "POST":
        #Attempt the user to sign in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        #Check if authentication is successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("information"))
        else:
            return render(request, "user_interface/loginRegister.html", {"message": "Invalid username or password. Please check again!"})
    else:
        return render(request, "user_interface/loginRegister.html", {"message": ""})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        #Ensure password matches the confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "user_interface/loginRegister.html", {"message": "Password not confirmed/matching. Please enter again."})

        #Attempt to create new USER
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "user_interface/loginRegister.html", {"message": "Username already exists."})
        
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "user_interface/loginRegister.html")




