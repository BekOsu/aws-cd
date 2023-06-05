from django.urls import path
from .views import EmployeeRetrieve

urlpatterns = [
    path('', EmployeeRetrieve.as_view(), name='EmployeeRetrieve')
]
