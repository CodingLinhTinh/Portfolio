from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("register", views.register_view, name='register'),
    path("create", views.form_createView, name='create'),
    path("create/information", views.introForm_createView, name='information'),
    path("create/education", views.eduForm_createView, name='education'),
    path("create/experience", views.expForm_createView, name='experience'),
    path("create/project", views.projectForm_createView, name='project'),
    path("create/skillset", views.skillForm_createView, name='skillset'),
    path("api/<str:username>", views.api_view, name='api'),
    path("<str:username>", views.portfolio_view, name='portfolio'),

    path("update/information", views.introForm_updateView, name='update_information'),
    path("update/education/<int:id>", views.eduForm_updateView, name='update_education'),
    path("update/experience/<int:id>", views.expForm_updateView, name='update_experience'),
    path("update/project/<int:id>", views.projectForm_updateView, name='update_project'),
    path("update/skillset/<int:id>", views.skillForm_updateView, name='update_skillset'),
    path("delete/information/<int:id>", views.information_deleteView, name='delete_information'),
    path("delete/education/<int:id>", views.education_deleteView, name='delete_education'),
    path("delete/experience/<int:id>", views.experience_deleteView, name='delete_experience'),
    path("delete/project/<int:id>", views.project_deleteView, name='delete_project'),
    path("delete/skillset/<int:id>", views.skillset_deleteView, name='delete_skillset'),
]