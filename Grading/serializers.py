from rest_framework import serializers
from .models import Grade




class GradeSerializer(serializers.ModelSerializer):
	def get_avg_grade(self, obj):
		return obj.get_avg_grade

	full_name = serializers.CharField(source='candidate', read_only='True')
	avg_grade = serializers.DecimalField(max_digits = 4, decimal_places = 2)
	
	class Meta:
		model = Grade
		fields = ['full_name', 'avg_grade']
