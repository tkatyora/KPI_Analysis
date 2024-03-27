# Generated by Django 5.0.3 on 2024-03-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kpi", "0009_commentreports_delete_finalcomment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentreports",
            name="body",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="commentreports",
            name="types",
            field=models.CharField(
                choices=[
                    ("comment", "Commnet"),
                    ("decision", "Decision"),
                    ("report", "Report"),
                    ("finalcom", "Final Commnet"),
                    ("finalde", "Final Decision"),
                ],
                default="Not Selected",
                max_length=100,
                null=True,
            ),
        ),
    ]