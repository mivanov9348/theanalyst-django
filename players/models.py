from django.db import models
from matches.models import Team

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()
    sport = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

class Stats(models.Model):
    athlete = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="stats")

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

    total_matches = models.IntegerField(default=0)
    total_goals = models.IntegerField(default=0)
    total_assists = models.IntegerField(default=0)
    total_yellow_cards = models.IntegerField(default=0)
    total_red_cards = models.IntegerField(default=0)

    avg_rating = models.FloatField(default=0)

    def update_stats(self):
        performances = self.athlete.match_performances.all()
        self.total_matches = performances.count()
        self.total_goals = sum(p.goals for p in performances)
        self.total_assists = sum(p.assists for p in performances)
        self.total_yellow_cards = sum(p.yellow_cards for p in performances)
        self.total_red_cards = sum(p.red_cards for p in performances)

        if performances.count() > 0:
            self.avg_rating = sum(p.match_rating for p in performances) / performances.count()
        else:
            self.avg_rating = 0

        self.save()
