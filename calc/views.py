from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django_socketio.example_project
from models import CalcLog


@login_required()
def dashboard(request):
    data = CalcLog.objects.all().values_list('equation', flat=True)
    return render(request, 'dashboard.html', {'ctx': data})
