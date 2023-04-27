from django.core.management.base import BaseCommand
from recipe_management.models import FoodItem
import csv

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Get all the food items from the database
        foods = FoodItem.objects.all()

        # # Filter Food based on user's profile
        # filter_foods = []
        # for food in foods:
        #     if food.calories <= max_calories and food.total_fat <= max_total_fat and food.cholesterol <= max_cholestrol and food.protein <= max_protein and food.carbohydratess <= max_carbohydrates and food.fiber <= max_fiber and food.sugars <= max_sugars:
        #         filter_foods.append(food)


        # define the food categories

        # groups = ['staple', 'bread', 'Snack', 'Side Dish', 'Dish']

        staple_foods = []
        bread_foods = []
        snack_foods = []
        side_dish_foods = []
        dish_foods = []

        for food in foods:
            if food.groups == 'Staple':
                staple_foods.append(food)
            elif food.groups == 'Bread':
                bread_foods.append(food)
            elif food.groups == 'Snack':
                snack_foods.append(food)
            elif food.groups == 'side Dish':
                side_dish_foods.append(food)
            else:
                dish_foods.append(food)

        # staple + dish + side dish
        sdsd_set = []
        for staple in staple_foods:
            for dish in dish_foods:
                for side_dish in side_dish_foods:
                    sdsd_set.append([staple.name, dish.name, side_dish.name, 
                                    staple.calories + dish.calories + side_dish.calories,
                                    staple.total_fat + dish.total_fat + side_dish.total_fat,
                                    staple.cholesterol + dish.cholesterol + side_dish.cholesterol,
                                    staple.protein + dish.protein + side_dish.protein,
                                    staple.carbohydrates + dish.carbohydrates + side_dish.carbohydrates,
                                    staple.fiber + dish.sfiber + side_dish.fiber,
                                    staple.sugars + dish.sugars + side_dish.sugars])

        # staple + dish

        sd_set = []
        for staple in staple_foods:
            for dish in dish_foods:
                sd_set.append([staple.name, dish.name, "", 
                                staple.calories + dish.calories,
                                staple.total_fat + dish.total_fat,
                                staple.cholesterol + dish.cholesterol,
                                staple.protein + dish.protein,
                                staple.carbohydrates + dish.carbohydrates,
                                staple.fiber + dish.fiber,
                                staple.sugars + dish.sugars])    
                        
            # bread + dish + side dish
        bdsd_set = []
        for bread in bread_foods:
            for dish in dish_foods:
                for side_dish in side_dish_foods:
                    sdsd_set.append([bread.name, dish.name, side_dish.name, 
                                    bread.calories + dish.calories + side_dish.calories,
                                    bread.total_fat + dish.total_fat + side_dish.total_fat,
                                    bread.cholesterol + dish.cholesterol + side_dish.cholesterol,
                                    bread.protein + dish.protein + side_dish.protein,
                                    bread.carbohydrates + dish.carbohydrates + side_dish.carbohydrates,
                                    bread.fiber + dish.sfiber + side_dish.fiber,
                                    bread.sugars + dish.sugars + side_dish.sugars])

        # bread + dish
        bd_set = []
        for bread in bread_foods:
                for dish in dish_foods:
                    bd_set.append([bread.name, dish.name, "", 
                                    bread.calories + dish.calories ,
                                    bread.total_fat + dish.total_fat,
                                    bread.cholesterol + dish.cholesterol,
                                    bread.protein + dish.protein,
                                    bread.carbohydrates + dish.carbohydrates,
                                    bread.fiber + dish.fiber,
                                    bread.sugars + dish.sugars])  
                        
        # snacks
        s_set = []
        for snack in snack_foods:
                s_set.append([snack.name, "", "", 
                                snack.calories,
                                snack.total_fat,
                                snack.cholesterol,
                                snack.protein,
                                snack.carbohydrates,
                                snack.fiber,
                                snack.sugars]) 
            
        breakfast_meal = []
        lunch_meal = []
        dinner_meal = []

        for lunch in sdsd_set:
            lunch_meal.append(lunch)

        for lunch in sd_set:
            lunch_meal.append(lunch)

        for dinner in bdsd_set:
            dinner_meal.append(dinner)

        for dinner in bd_set:
            dinner_meal.append(dinner)

        for breakfast in s_set:
            breakfast_meal.append(breakfast)

        with open("lunch_meal.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # write the header row
            writer.writerow(["food1", "food2", "food3", "calories", "total_fat", "cholesterol", "protein",
                            "carbohydrates", "fiber", "sugars"])
            
            writer.writerows(lunch_meal)

        with open("dinner_meal.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # write the header row
            writer.writerow(["food1", "food2", "food3", "calories", "total_fat", "cholesterol", "protein",
                            "carbohydrates", "fiber", "sugars"])
            
            writer.writerows(dinner_meal)

        with open("breakfast_meal.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # write the header row
            writer.writerow(["food1", "food2", "food3", "calories", "total_fat", "cholesterol", "protein",
                            "carbohydrates", "fiber", "sugars"])
            
            writer.writerows(breakfast_meal)