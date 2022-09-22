# Generated by Django 4.1.1 on 2022-09-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=100)),
                ('molienda', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Metodos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gramos', models.IntegerField()),
            ],
        ),
    ]
