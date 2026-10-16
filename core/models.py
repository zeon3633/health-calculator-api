from django.db import models
from django.contrib.auth.models import User

# Модель для хранения истории расчетов
class CalculationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history')
    bmi = models.FloatField(verbose_name="ИМТ")
    bmi_status = models.CharField(max_length=50, verbose_name="Статус ИМТ")
    bmr_kcal = models.IntegerField(verbose_name="BMR (ккал)")
    daily_calories = models.IntegerField(verbose_name="Суточная норма калорий")
    water_liters = models.FloatField(verbose_name="Норма воды (л)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата расчета")

    class Meta:
        verbose_name = "История расчета"
        verbose_name_plural = "История расчетов"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"