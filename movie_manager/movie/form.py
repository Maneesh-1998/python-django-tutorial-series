from django.forms import ModelForm
from . models import *
class MovieForm(ModelForm):
    class Meta:
        model=MovieInfo
        fields='__all__'