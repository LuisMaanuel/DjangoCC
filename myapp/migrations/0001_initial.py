# Generated by Django 4.2.7 on 2023-11-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=100)),
                ('nodos', models.CharField(max_length=100)),
                ('num_cores', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('almacenamiento', models.CharField(max_length=100)),
                ('teraFlops', models.CharField(max_length=100)),
                ('SO', models.CharField(max_length=100)),
            ],
        ),
    ]
