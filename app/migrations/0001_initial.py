# Generated by Django 4.2.6 on 2024-01-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('zoo', models.CharField(max_length=100)),
                ('aid', models.IntegerField()),
                ('re_enter', models.IntegerField()),
            ],
        ),
    ]
