from django.forms import ModelForm
from .models import Grade


class AddMark(ModelForm):
	class Meta:
		model = Grade
		fields = ['value', 'task', 'candidate', 'recruiter']
		