from django.contrib import admin

# Register your models here.
from .models import Candidate, Recruiter, Grade, Task

admin.site.register(Candidate)
admin.site.register(Recruiter)
admin.site.register(Task)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
	list_display = ["candidate", "task", "value"]
	list_filter = ("candidate",)