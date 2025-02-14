from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report
from athletes.models import Athlete

@login_required
def create_report(request):
    athletes = Athlete.objects.all()

    if request.method == "POST":
        athlete_id = request.POST.get("athlete")
        speed = request.POST.get("speed_rating")
        strength = request.POST.get("strength_rating")
        endurance = request.POST.get("endurance_rating")
        ball_control = request.POST.get("ball_control_rating")
        passing = request.POST.get("passing_rating")
        shooting = request.POST.get("shooting_rating")
        positioning = request.POST.get("positioning_rating")
        vision = request.POST.get("vision_rating")
        aggression = request.POST.get("aggression_rating")
        composure = request.POST.get("composure_rating")
        report_text = request.POST.get("report_text")

        athlete = get_object_or_404(Athlete, id=athlete_id)

        report = Report.objects.create(
            athlete=athlete,
            author=request.user,
            speed_rating=speed,
            strength_rating=strength,
            endurance_rating=endurance,
            ball_control_rating=ball_control,
            passing_rating=passing,
            shooting_rating=shooting,
            positioning_rating=positioning,
            vision_rating=vision,
            aggression_rating=aggression,
            composure_rating=composure,
            report_text=report_text,
        )

        return redirect("dashboard")

    return render(request, "reports/create_report.html", {"athletes": athletes})
