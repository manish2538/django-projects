from django.contrib import admin
from resume.models import Contact
from resume.models import Resume
from resume.models import Post
from resume.models import Project
# Register your models here.
admin.site.register(Contact)
admin.site.register(Resume)
admin.site.register(Post)
admin.site.register(Project)