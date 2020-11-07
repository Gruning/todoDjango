from django.forms import ModelForm
from django.forms import fields
from .models import Todo
class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields=['title','memo','important']