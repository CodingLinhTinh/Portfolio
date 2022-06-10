from django.contrib import admin
from .models import (   User, 
                        InformationModel,
                        EducationModel,
                        ExperienceModel,
                        SkillsetModel,
                        ProjectModel,
                        MessageModel )

# Register your models here.

admin.site.register(User)
admin.site.register(InformationModel)
admin.site.register(EducationModel)
admin.site.register(ExperienceModel)
admin.site.register(SkillsetModel)
admin.site.register(ProjectModel)
admin.site.register(MessageModel)

