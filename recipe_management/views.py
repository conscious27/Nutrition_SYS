from django.shortcuts import render
from django.contrib.auth import get_user_model
from user_management.models import Profile
from .models import Breakfast_meal, Lunch_meal, Dinner_meal
import time

import itertools
# Create your views here.

# class Profile_limit:
#     def __init__(self, user):
#         self.user = user

#         self.max_calorie = (10 * self.user.weight) + (6.25 * self.user.height) - (5 * self.user.age) + 5


def generate_recommendation(request):

    start_time = time.time()
    user_profile = Profile.objects.get(user = request.user)
    BMR = float((10 * user_profile.weight)) + (6.25 * float(user_profile.height)) - (5 * user_profile.age)
    
    max_calories = (BMR * float(user_profile.physical_activity))
    max_calories = max_calories - (10/100 * max_calories)
    max_total_fat = (30/100 * max_calories)/9

    if user_profile.cholesterol_level == None:
        max_cholesterol = 300 - (user_profile.age/20)
    else:
        max_cholesterol = 200 - (user_profile.cholesterol_level/2)

    if user_profile.physical_activity == 1.4:
        protein_factor = 0.8
    elif user_profile.physical_activity == 1.6:
        protein_factor = 1.0
    elif user_profile.physical_activity == 1.8:
        protein_factor = 1.2
    elif user_profile.physical_activity == 2.0:
        protein_factor = 1.4
    else:
        protein_factor = 1.8

    max_protein = float(user_profile.weight) * protein_factor

    TDEE = BMR * float(user_profile.physical_activity)

    max_carbohydrates = (TDEE * 50)/4
    max_sugars = (max_calories * 0.1)/4
    max_fiber = 25

    breakfasts = Breakfast_meal.objects.all()
    lunches = Lunch_meal.objects.all()
    dinners = Dinner_meal.objects.all()
    end_time = time.time()

    print("time taken for first piece of code: ", end_time - start_time)

    begin_time = time.time()
    recommended_meal = (
        [breakfast.food1, breakfast.food2, breakfast.food3,
        lunch.food1, lunch.food2, lunch.food3,
        dinner.food1, dinner.food2, dinner.food3]
        for breakfast in breakfasts
        for lunch in lunches
        for dinner in dinners
        if breakfast.calories + lunch.calories + dinner.calories <= max_calories
        and breakfast.total_fat + lunch.total_fat + dinner.total_fat <= max_total_fat
        and breakfast.cholesterol + lunch.cholesterol + dinner.cholesterol <= max_cholesterol
        and breakfast.protein + lunch.protein + dinner.protein <= max_protein
        and breakfast.carbohydrates + lunch.carbohydrates + dinner.carbohydrates <= max_carbohydrates
        and breakfast.fiber + lunch.fiber + dinner.fiber <= max_fiber
        and breakfast.sugars + lunch.sugars + dinner.sugars <= max_sugars
    )

    finish_time = time.time()

    print("time taken for second piece of code", finish_time - begin_time)
    # context = { "recommended_meal" : recommended_meal }

    print("somewhat successful!")

    # slice the first 5 meals from the generator and convert them to a list
    recommended_meals_list = list(itertools.islice(recommended_meal, 7))

    print(recommended_meals_list)
    # create a context dictionary to pass the data to the template
    context = {'recommended_meals': recommended_meals_list}

    # render the template with the context dictionary
    return render(request, 'recommended_meal.html', context)

    # return  render(request, "recommended_meal.html", context)