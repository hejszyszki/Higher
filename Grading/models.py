from django.db import models
from django.utils.translation import gettext as _
from django.db.models import Avg
# Create your models here.
class Candidate(models.Model):
	first_name 	= models.CharField(max_length=30)
	last_name   = models.CharField(max_length=30)

	def __str__(self):
		return self.first_name + ' ' + self.last_name 
	
	

class Recruiter(models.Model):
	first_name 	= models.CharField(max_length=30)
	last_name   = models.CharField(max_length=30)

	def __str__(self):
		return self.first_name + ' ' + self.last_name 

class Task(models.Model):
	title = models.CharField(max_length=40, unique=True)

	def __str__(self):
		return self.title

class Grade(models.Model):
	F=1
	E=2  
	D=3
	C=4
	B=5
	A=6
	GV=(
		(F, _('1')),
		(E, _('2')),
		(D, _('3')),
		(C, _('4')),
		(B, _('5')),
		(A, _('6')),
		)
	value = models.PositiveSmallIntegerField(
		choices=GV,
		)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	recruiter = models.ForeignKey(Recruiter, on_delete=models.SET_NULL, null=True)

	class Meta:
		unique_together = ('task', 'candidate')
		
	def __str__(self):
		return str(self.candidate) + ' ' + str(self.task)

	