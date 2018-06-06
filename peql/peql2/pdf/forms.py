from django import forms
from .models import Pdf

class FormularioDocumento(forms.ModelForm):
	class Meta:
		model = Pdf
		fields = ('Nombre', 'Upload')