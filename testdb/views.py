from django.views.generic.list import ListView
from .models import Profile


class EmployeeRetrieve(ListView):
    model = Profile