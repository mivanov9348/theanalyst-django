import pandas as pd
from athletes.models import Stats, Athlete

def export_to_excel():
    stats = Stats.objects.all().values()
    df = pd.DataFrame(stats)
    df.to_excel("athlete_report.xlsx", index=False)
