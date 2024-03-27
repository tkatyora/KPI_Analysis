# Generated by Django 5.0.3 on 2024-03-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kpi", "0003_remove_user_nationalid"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.CharField(
                choices=[
                    ("Harare", "Harare"),
                    ("Bulawayo", "Bulawayo"),
                    ("Gweru", "Gweru"),
                    ("Chitungwiza", "Chitungwiza"),
                    ("Mutare", "Mutare"),
                    ("Kwekwe", "Kwekwe"),
                    ("Kadoma", "Kadoma"),
                    ("Masvingo", "Masvingo"),
                    ("Norton", "Norton"),
                    ("Chinhoyi", "Chinhoyi"),
                ],
                default="Not Selected",
                max_length=100,
                null=True,
            ),
        ),
    ]