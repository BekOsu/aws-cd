from django.views.generic.list import ListView
from .models import Employee


class EmployeeRetrieve(ListView):
    model = Employee