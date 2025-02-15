from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Report(models.Model):
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name="reports")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")

    speed_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    strength_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    endurance_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    ball_control_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    passing_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    shooting_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    positioning_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    vision_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    aggression_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    composure_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

    report_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report on {self.player.first_name} {self.player.last_name} by {self.author.username}"
