# Generated by Django 4.0.5 on 2022-06-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
