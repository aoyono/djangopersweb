# Generated by Django 3.2.6 on 2021-08-14 06:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('texte', models.TextField()),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_publication', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
