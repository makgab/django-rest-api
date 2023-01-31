# Generated by Django 4.1.5 on 2023-01-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=20)),
                ('local_currency', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
