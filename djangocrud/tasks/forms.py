from django.forms import ModelForm
from .models import Task # type: ignore

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']