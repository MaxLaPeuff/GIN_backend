# Generated by Django 5.2 on 2025-05-12 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Formation",
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
                ("titre", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("objectifs", models.JSONField(default=list)),
                ("programme", models.JSONField(default=list)),
                ("prerecquis", models.JSONField(default=list)),
                ("acquis", models.TextField(verbose_name="acquis")),
                ("debouche", models.TextField(verbose_name="Débouchés")),
                ("prix", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_debut", models.DateField()),
                ("date_fin", models.DateField(blank=True, null=True)),
                ("lieu", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="InscriptionFormation",
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
                ("nom", models.CharField(max_length=100)),
                ("prenom", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("motivations", models.TextField()),
                (
                    "dernier_diplome",
                    models.CharField(
                        choices=[
                            ("BEPC", "BEPC"),
                            ("BAC", "Bac"),
                            ("LICENCE", "Licence"),
                            ("MASTER", "Master"),
                            ("DOCTORAT", "Doctorat"),
                        ],
                        max_length=10,
                    ),
                ),
                ("domaine", models.CharField(max_length=100)),
                ("annees_experience", models.PositiveIntegerField()),
                (
                    "formation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="inscriptions",
                        to="gin.formation",
                    ),
                ),
            ],
        ),
    ]
