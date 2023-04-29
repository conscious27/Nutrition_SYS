from django.shortcuts import render
# from django.contrib.auth import get_user_model
from user_management.models import Profile
from .models import Breakfast_meal, Lunch_meal, Dinner_meal
from .models import BreakfastMealFeedback, LunchMealFeedback, DinnerMealFeedback
import random
from django.db.models import Q

# import itertools
# Create your views here.

# class Profile_limit:
#     def __init__(self, user):
#         self.user = user

#         self.max_calorie = (10 * self.user.weight) + (6.25 * self.user.height) - (5 * self.user.age) + 5


def generate_recommendation(request):

    if not request.user.is_authenticated:
        return render(request, "login.html")
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

    # slice the first 5 meals from the generator and convert them to a list
    # recommended_meals_list = list(itertools.islice(recommended_meal, 7))

    # print(recommended_meals_list)
    # # create a context dictionary to pass the data to the template
    # context = {'recommended_meals': recommended_meals_list}

    # # render the template with the context dictionary
    # return render(request, 'recommended_meal.html', context)

    # return  render(request, "recommended_meal.html", context)

    breakfast_options = Breakfast_meal.objects.all()
    lunch_options = Lunch_meal.objects.all()
    dinner_options = Dinner_meal.objects.all()

    # Combine all meal options into one list
    meal_options = list(breakfast_options) + list(lunch_options) + list(dinner_options)

    # Filter out meal options that exceed user's maximum nutrient values
    # meal_options = meal_options.filter(
    #     Q(calories__lte=max_calories) &
    #     Q(total_fat__lte=max_total_fat) &
    #     Q(carbohydrate__lte=max_carbohydrates) &
    #     Q(fiber__lte=max_fiber) &
    #     Q(sugars__lte=max_sugars) &
    #     Q(cholesterol__lte=max_cholesterol) &
    #     Q(proteins__lte=max_protein) 
    # )

    user_breakfast_likes = BreakfastMealFeedback.objects.filter(Q(like=True) | Q(dislike=True), user=user_profile.user)
    user_lunch_likes = LunchMealFeedback.objects.filter(Q(like=True) | Q(dislike=True), user=user_profile.user)
    user_dinner_likes = DinnerMealFeedback.objects.filter(Q(like=True) | Q(dislike=True), user=user_profile.user)

    for user_like in user_breakfast_likes:
        if user_like.like == False:
            meal_options = meal_options.exclude(id=user_like.breakfast_meal.id)

    for user_like in user_lunch_likes:
        if user_like.like == False:
            meal_options = meal_options.exclude(id=user_like.lunch_meal.id)

    for user_like in user_dinner_likes:
        if user_like.like == False:
            meal_options = meal_options.exclude(id=user_like.dinner_meal.id)

    weekly_meals = []
    for _ in range(7):

        breakfast = random.choice(breakfast_options)
        lunch = random.choice(lunch_options)
        dinner = random.choice(dinner_options)

        # Combine the nutrient values of all three meals
        combined_nutrients = {
            'Total_Calories': breakfast.calories + lunch.calories + dinner.calories,
            'Total_Fat': breakfast.total_fat + lunch.total_fat + dinner.total_fat,
            'Total_Carbohydrate': breakfast.carbohydrates + lunch.carbohydrates + dinner.carbohydrates,
            'Total_Fiber': breakfast.fiber + lunch.fiber + dinner.fiber,
            'Total_Sugars': breakfast.sugars + lunch.sugars + dinner.sugars,
            'Total_Cholesterol': breakfast.cholesterol + lunch.cholesterol + dinner.cholesterol,
            'Total_Proteins': breakfast.protein + lunch.protein + dinner.protein,
        }

        # Check if the combined nutrient values exceed user's maximum nutrient values
        if combined_nutrients['Total_Calories'] > max_calories and combined_nutrients['Total_Fat'] > max_total_fat and \
            combined_nutrients['Total_Carbohydrate'] > max_carbohydrates and combined_nutrients['Total_Sugars'] > max_sugars and \
            combined_nutrients['Total_Cholesterol'] > max_cholesterol and combined_nutrients['Total_Proteins'] > max_protein:
            # If the combined nutrient values exceed user's maximum nutrient values, skip this combination
            continue

        # Append the selected meals to weekly meals list
        weekly_meals.append({
            'breakfast_food1': breakfast.food1,
            'breakfast_food2': breakfast.food2,
            'breakfast_food3': breakfast.food3,
            'lunch_food1': lunch.food1,
            'lunch_food2': lunch.food2,
            'lunch_food3': lunch.food3,
            'dinner_food1': dinner.food1,
            'dinner_food2': dinner.food2,
            'dinner_food3': dinner.food3,
            'nutrients': combined_nutrients,
        })

    context = {'weekly_meals' : weekly_meals}

    return render(request, 'recommended_meal.html', context)