from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import CalculationHistory
from .serializers import CalculationHistorySerializer

# 1. Расчет и сохранение
class CalculateHealthMetricsView(APIView):
    permission_classes = [IsAuthenticated] # Требует JWT-токен

    def post(self, request):
        data = request.data
        
        # Получаем данные из запроса
        gender = data.get('gender', 'female') # 'female' или 'male'
        age = int(data.get('age', 25))
        height = float(data.get('height', 168))
        weight = float(data.get('weight', 58))
        activity_level = float(data.get('activity_level', 1.55))

        # 1. Расчет ИМТ
        bmi = round(weight / ((height / 100) ** 2), 1)
        bmi_status = 'Норма'
        if bmi < 18.5:
            bmi_status = 'Дефицит массы'
        elif 25 <= bmi < 30:
            bmi_status = 'Избыточная масса'
        elif bmi >= 30:
            bmi_status = 'Ожирение'

        # 2. Расчет BMR (Миффлин-Сан Жеор)
        bmr = 10 * weight + 6.25 * height - 5 * age
        bmr_kcal = round(bmr - 161 if gender == 'female' else bmr + 5)

        # 3. Суточная норма калорий и воды
        daily_calories = round(bmr_kcal * activity_level)
        water_liters = round((weight * 35) / 1000, 1)

        # Сохраняем в PostgreSQL для авторизованного юзера
        record = CalculationHistory.objects.create(
            user=request.user,
            bmi=bmi,
            bmi_status=bmi_status,
            bmr_kcal=bmr_kcal,
            daily_calories=daily_calories,
            water_liters=water_liters
        )

        serializer = CalculationHistorySerializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 2. Получение всей истории расчетов пользователя
class CalculationHistoryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        history = CalculationHistory.objects.filter(user=request.user)
        serializer = CalculationHistorySerializer(history, many=True)
        return Response(serializer.data)