from django.core.management.base import BaseCommand
import csv
from recipe_management.models import Breakfast_meal, Lunch_meal, Dinner_meal, Day_meal

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        breakfasts = Breakfast_meal.objects.all()
        lunches = Lunch_meal.objects.all()
        dinners = Dinner_meal.objects.all()

        per_day_meal_set = [            [breakfast.food1, breakfast.food2, breakfast.food3,             
                                         lunch.food1, lunch.food2, lunch.food3,             
                                         dinner.food1, dinner.food2, dinner.food3,             
                                         breakfast.calories + lunch.calories + dinner.calories,             
                                         breakfast.total_fat + lunch.total_fat + dinner.total_fat,             
                                         breakfast.cholesterol + lunch.cholesterol + dinner.cholesterol,             
                                         breakfast.protein + lunch.protein + dinner.protein,             
                                         breakfast.carbohydrates + lunch.carbohydrates + dinner.carbohydrates,             
                                         breakfast.fiber + lunch.fiber + dinner.fiber,             
                                         breakfast.sugars + lunch.sugars + dinner.sugars]
            for breakfast in breakfasts
            for lunch in lunches
            for dinner in dinners
        ]

        # create Day_meal objects in bulk
        day_meal_objects = [            Day_meal(                
                breakfast_food1=item[0], breakfast_food2=item[1], breakfast_food3=item[2],
                lunch_food1=item[3], lunch_food2=item[4], lunch_food3=item[5],
                dinner_food1=item[6], dinner_food2=item[7], dinner_food3=item[8],
                total_calories=item[9], total_fat=item[10], total_cholesterol=item[11],
                total_protein=item[12], total_carbohydrates=item[13], total_fiber=item[14],
                total_sugars=item[15]
            )
            for item in per_day_meal_set
        ]

        # bulk create Day_meal objects
        Day_meal.objects.bulk_create(day_meal_objects)
