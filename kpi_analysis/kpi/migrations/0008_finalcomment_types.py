# Generated by Django 5.0.3 on 2024-03-19 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kpi", "0007_alter_user_roles_finalcomment"),
    ]

    operations = [
        migrations.AddField(
            model_name="finalcomment",
            name="types",
            field=models.CharField(
                choices=[("comment", "Commnet"), ("decision", "Decision")],
                default="Not Selected",
                max_length=100,
                null=True,
            ),
        ),
    ]