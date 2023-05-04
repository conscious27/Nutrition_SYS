from django.core.management.base import BaseCommand
import csv
from recipe_management.models import Breakfast_meal, Lunch_meal, Dinner_meal

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to load')
        parser.add_argument('model_name', type=str, help='The name of the Django model to load the data into')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        model_name = options['model_name']

        # Import the appropriate Django model based on the given name
        if model_name == 'Breakfast_meal':
            model = Breakfast_meal
        elif model_name == 'Lunch_meal':
            model = Lunch_meal
        elif model_name == 'Dinner_meal':
            model = Dinner_meal
        else:
            raise ValueError(f'Invalid model name: {model_name}')

        # Open the CSV file and create a CSV reader
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  # get the header row

            # Map the header columns to the model field names
            field_map = {header[i]: model._meta.get_field(field).name for i, field in enumerate(header)}

            # Loop over the remaining rows and create instances of the model
            for row in reader:
                # Create a dictionary of the field names and values
                fields = {field_map[key]: value for key, value in zip(header, row)}

                # Create a new instance of the model and populate the fields
                instance = model(**fields)

                # Save the instance to the database
                instance.save()

        # Print a success message
        self.stdout.write(self.style.SUCCESS(f'Data loaded successfully into {model_name}'))

