from django.shortcuts import render
from user_management.models import Profile
from .models import Breakfast_meal, Lunch_meal, Dinner_meal, FoodItem
from .models import BreakfastMealFeedback, LunchMealFeedback, DinnerMealFeedback
import random
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse

def generate_recommendation(request):

    # get user profile
    if not request.user.is_authenticated:
        return render(request, "login.html")
    user_profile = Profile.objects.get(user = request.user)

    # start caluclating maximum limit for every nutrients user should have
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

    breakfast_options = Breakfast_meal.objects.all()
    lunch_options = Lunch_meal.objects.all()
    dinner_options = Dinner_meal.objects.all()

    # # check if user likes or dikslikes any meal option
    # user_breakfast_likes = BreakfastMealFeedback.objects.filter(Q(like=True) | Q(dislike=True), user=user_profile.user)
    # user_lunch_likes = LunchMealFeedback.objects.filter(Q(like=True) | Q(dislike=True), user=user_profile.user)
    # user_dinner_likes = DinnerMealFeedback.objects.filter(Q(like=True) | Q(dislike=True), user=user_profile.user)

    # # if dislike remove it from consideration
    # for user_like in user_breakfast_likes:
    #     if user_like.like == False:
    #         breakfast_options = breakfast_options.exclude(id=user_like.breakfast_meal.id)

    # for user_like in user_lunch_likes:
    #     if user_like.like == False:
    #         lunch_options = lunch_options.exclude(id=user_like.lunch_meal.id)

    # for user_like in user_dinner_likes:
    #     if user_like.like == False:
    #         dinner_options = dinner_options.exclude(id=user_like.dinner_meal.id)

    # check meal score if negative remove it from consideration

    for breakfast in breakfast_options:
        if breakfast.score < 0:
            breakfast_options = breakfast_options.exclude(id=breakfast.id)

    for lunch in lunch_options:
        if lunch.score < 0:
            lunch_options = lunch_options.exclude(id=lunch.id)

    for dinner in lunch_options:
        if dinner.score < 0:
            dinner_options = dinner_options.exclude(id=dinner.id)

    foods = FoodItem.objects.all()

    # if user is not allowed remove from consideration
    for meal in breakfast_options:
        meal_food1 = meal.food1
        meal_food2 = meal.food2
        meal_food3 = meal.food3
        for food in foods:
            if food.name == meal_food1 or food.name == meal_food2 or food.name == meal_food3:
                if food.category1 == user_profile.dietary_restriction or food.category2 == user_profile.dietary_restriction:
                    breakfast_options = breakfast_options.exclude(food1=food.name)
                    breakfast_options = breakfast_options.exclude(food2=food.name)
                    breakfast_options = breakfast_options.exclude(food3=food.name)

    for meal in lunch_options:
        meal_food1 = meal.food1
        meal_food2 = meal.food2
        meal_food3 = meal_food3
        for food in foods:
            if food.name == meal_food1 or food.name == meal_food2 or food.name == meal_food3:
                if food.category1 == user_profile.dietary_restriction or food.category2 == user_profile.dietary_restriction:
                    lunch_options = lunch_options.exclude(food1=food.name)
                    lunch_options = lunch_options.exclude(food2=food.name)
                    lunch_options = lunch_options.exclude(food3=food.name)

    for meal in dinner_options:
        meal_food1 = meal.food1
        meal_food2 = meal.food2
        meal_food3 = meal_food3
        for food in foods:
            if food.name == meal_food1 or food.name == meal_food2 or food.name == meal_food3:
                if food.category1 == user_profile.dietary_restriction or food.category2 == user_profile.dietary_restriction:
                    dinner_options = dinner_options.exclude(food1=food.name)
                    dinner_options = dinner_options.exclude(food2=food.name)
                    dinner_options = dinner_options.exclude(food3=food.name)

    # get top 3 highest scoring meal options for each meal type
    top_breakfast_options = list(breakfast_options.order_by('-score')[:3])
    top_lunch_options = list(lunch_options.order_by('-score')[:3])
    top_dinner_options = list(dinner_options.order_by('-score')[:3])


    # check if any top 3 options have score=0, if yes, choose all random meals
    if any(option.score == 0 for option in top_breakfast_options):
        top_breakfast_options = []

    if any(option.score == 0 for option in top_lunch_options):
        top_lunch_options = []
    
    if any(option.score == 0 for option in top_dinner_options):
        top_dinner_options = []

    # randomly choose 4 other meal options for each meal type
    other_breakfast_options = list(breakfast_options.exclude(id__in=[option.id for option in top_breakfast_options]))
    random_breakfast_options = random.sample(other_breakfast_options, k=min(4, len(other_breakfast_options)))

    other_lunch_options = list(lunch_options.exclude(id__in=[option.id for option in top_lunch_options]))
    random_lunch_options = random.sample(other_lunch_options, k=min(4, len(other_lunch_options)))

    other_dinner_options = list(dinner_options.exclude(id__in=[option.id for option in top_dinner_options]))
    random_dinner_options = random.sample(other_dinner_options, k=min(4, len(other_dinner_options)))

    # weekly mdinner
    weekly_meals = []

    # getting 7 random meal set for all three options
    for _ in range(7):

        # choose any random meal option
        breakfast = random.choice(top_breakfast_options + random_breakfast_options) if top_breakfast_options else random.choice(random_breakfast_options)
        lunch = random.choice(top_lunch_options + random_lunch_options) if top_lunch_options else random.choice(random_lunch_options)
        dinner = random.choice(top_dinner_options + random_dinner_options) if top_dinner_options else random.choice(random_dinner_options)

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
            combined_nutrients['Total_Cholesterol'] > max_cholesterol and combined_nutrients['Total_Proteins'] > max_protein and \
            combined_nutrients['Total_Fiber'] > max_fiber:
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

    # sort all weekly meal in the context
    context = {'weekly_meals' : weekly_meals}

    return render(request, 'recommended_meal.html', context)

# @csrf_exempt
# def dislike_meal(request, meal_id):
#     if request.method != 'POST':
#         return HttpResponseBadRequest('Only POST request are allowed.')
    
#     try:
#         meal = Breakfast_meal.objects.get(id=meal_id)
#     except Breakfast_meal.DoesNotExist:
#         return HttpResponseBadRequest('Meal not found.')
    

#     # Update the meal score
#     meal.score -= 1
#     meal.save()

#     return JsonResponse({'success' : True})

def display_recipe(request, recipe_name):
    try:
        with open(f"static/recipe/{recipe_name}.txt", "r") as recipe_file:
            recipe_text = recipe_file.read()
    except FileNotFoundError:
        return HttpResponseNotFound("Recipe not found")

    context = {"recipe_text": recipe_text}
    return render(request, "recipe.html", context)