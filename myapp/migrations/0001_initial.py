# Generated by Django 4.1 on 2022-09-02 16:05

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuoteTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quote", models.TextField(max_length=300)),
                ("qauthor", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "qtype",
                    models.CharField(
                        choices=[
                            ("Motivational", "Motivational"),
                            ("Success", "success"),
                            ("Friendship", "Friendship"),
                            ("Inspirational", "Inspirational"),
                            ("Positive", "Positive"),
                            ("Life", "Life"),
                            ("Wisdom", "Wisdom"),
                            ("Faith", "Faith"),
                            ("Freedom", "Freedom"),
                        ],
                        default="Motivational",
                        max_length=20,
                    ),
                ),
                ("qimage", models.ImageField(upload_to="uploaded")),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
        ),
    ]
