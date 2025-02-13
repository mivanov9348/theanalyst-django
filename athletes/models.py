from django.db import models

class Athlete(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()
    sport = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    team = models.CharField(max_length=50, null=True, blank=True)

class Stats(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    performance_score = models.FloatField()
