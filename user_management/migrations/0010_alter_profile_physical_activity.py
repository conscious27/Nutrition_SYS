# Generated by Django 4.1.2 on 2023-05-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0009_alter_profile_physical_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='physical_activity',
            field=models.DecimalField(choices=[(1.4, 'sedentary_lifestyle'), (1.6, 'low_active_lifestyle'), (1.8, 'moderate_lifestyle'), (2.0, 'active_lifestyle'), (2.2, 'very_active_lifestyle')], decimal_places=2, max_digits=6),
        ),
    ]
