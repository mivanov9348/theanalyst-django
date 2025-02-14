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

class Match(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    def __str__(self):
        return f"{self.home_team} {self.home_score} - {self.away_score} {self.away_team} ({self.date})"

class MatchPerformance(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="performances")
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name="match_performances")

    minutes_played = models.IntegerField()
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    passes_completed = models.IntegerField(default=0)
    shots_on_target = models.IntegerField(default=0)
    tackles_made = models.IntegerField(default=0)
    match_rating = models.FloatField()

    def __str__(self):
        return f"{self.athlete.first_name} {self.athlete.last_name} - {self.match} ({self.match_rating}/10)"