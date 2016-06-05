from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import logout as django_logout
from calc.models import CalcLog


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):

        try:
            path = '/dashboard/'
            request.session['email_id'] = request.user.email
        except AttributeError:
            django_logout(request)
            request.session.flush()
            path = '/'
        return path

    def get_logout_redirect_url(self, request):
        path = '/'
        CalcLog.objects.filter(user_id=request.user.id).delete()
        django_logout(request)
        request.session.flush()
        return path

    def logout(self, request):
        CalcLog.objects.filter(user_id=request.user.id).delete()
        django_logout(request)
