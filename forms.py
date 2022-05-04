from django import forms
from .models import ComingSoonNotice

class ComingSoonForm(forms.ModelForm):
	class Meta:
		model =  ComingSoonNotice
		fields = ("name", "email")