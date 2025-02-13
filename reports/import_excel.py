import pandas as pd
from athletes.models import Stats, Athlete

def import_excel(file_path):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        athlete = Athlete.objects.get(id=row['athlete_id'])
        Stats.objects.create(
            athlete=athlete,
            matches_played=row['matches_played'],
            wins=row['wins'],
            losses=row['losses'],
            performance_score=row['performance_score']
        )
