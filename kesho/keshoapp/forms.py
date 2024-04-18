from django.forms import ModelForm
from .models import *

class AddbabeForm(ModelForm):
    class Meta:
        model = Babe
        fields = '__all__'