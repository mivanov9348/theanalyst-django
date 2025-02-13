from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ['author', 'created_at']
        widgets = {
            'report_text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter scouting report'}),
        }
