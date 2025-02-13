from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user_role = request.user.role
    return render(request, 'core/dashboard.html', {'role': user_role})  # Ако темплейтът е преместен, смени пътя
