from django.urls import path
from Grading.views import adding

urlpatterns = [
	path('addmark/', adding)
	]
    
