from django.http import HttpResponseRedirect
from django.shortcuts import render


def login_view(request):
    if request.session.get('email_id'):
        return HttpResponseRedirect('/dashboard')
    return render(request, 'login.html', {})