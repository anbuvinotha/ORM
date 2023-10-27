from django.db import models
from django.contrib import admin
class Footballplayer (models.Model):
    teamname=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    goals=models.IntegerField()
    jersey=models.IntegerField()


class FootballplayerAdmin(admin.ModelAdmin):
    list_display=('teamname','name','age','goals','jersey')
