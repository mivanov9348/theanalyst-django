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
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name="stats")

    speed = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    strength = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    endurance = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    ball_control = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    passing = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    shooting = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    positioning = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    vision = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    aggression = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    composure = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

    matches_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    performance_score = models.FloatField()
