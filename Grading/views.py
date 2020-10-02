from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import AddMark
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import GradeSerializer
from .models import Grade
from django.db.models import Avg

# Create your views here.

def adding(request):
	mark = AddMark(request.POST)

	if mark.is_valid():
		mark.save()

	return render(request, 'addmark.html', {'mark': mark})

class GradeView(viewsets.ModelViewSet):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializer

	def get_queryset(self):
		return Grade.objects.annotate(
			avg_grade = Avg('value'))
