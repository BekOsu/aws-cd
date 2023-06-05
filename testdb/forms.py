from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        # To specify the model to be used to create form
        model = Employee
        # It includes all the fields of model
        fields = '__all__'
