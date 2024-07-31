from django.contrib import admin
from .models import Profile, Resume, Feedback,Project,Education,Skill
import os
# Register your models here.


class MyModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # Check if this is an existing object (change=True) and has a file
        if change:
            try:
                old_obj = Resume.objects.get(pk=obj.pk)
                # If the file has been changed, delete the old file
                if old_obj.resume_file and old_obj.resume_file.name:
                    storage = old_obj.resume_file.storage
                    if storage.exists(old_obj.resume_file.name):
                        storage.delete(old_obj.resume_file.name)
            except Resume.DoesNotExist:
                pass
        
        # Save the new or updated object
        super().save_model(request, obj, form, change)


admin.site.register(Profile)
admin.site.register(Resume,MyModelAdmin)
admin.site.register(Feedback)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Skill)