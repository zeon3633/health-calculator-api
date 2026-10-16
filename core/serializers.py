from rest_framework import serializers
from .models import CalculationHistory

class CalculationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationHistory
        fields = ['id', 'bmi', 'bmi_status', 'bmr_kcal', 'daily_calories', 'water_liters', 'created_at']