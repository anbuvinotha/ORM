# Generated by Django 4.2.6 on 2023-10-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footballplayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('jersey', models.IntegerField()),
            ],
        ),
    ]