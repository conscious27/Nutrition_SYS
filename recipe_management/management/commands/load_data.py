from django.core.management.base import BaseCommand, CommandError
import csv
from recipe_management.models import FoodItem


class Command(BaseCommand):
    help = 'Load data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for row in reader:
                # create a new instance of your model and save it to the database
                instance = FoodItem(
                    name=row[0],
                    groups=row[1],
                    calories=float(row[2]),
                    total_fat=float(row[3]),
                    saturated_fat=float(row[4]),
                    cholesterol=float(row[5]),
                    protein=float(row[6]),
                    carbohydrates=float(row[7]),
                    fiber=float(row[8]),
                    sugars=float(row[9]),
                    category1=row[10],
                    category2=row[11]
                    # add more fields as needed
                )
                instance.save()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
