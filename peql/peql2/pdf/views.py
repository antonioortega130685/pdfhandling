from django.shortcuts import render, redirect
from .models import Pdf
from .forms import FormularioDocumento

from django.http import HttpResponse
from django.views import View

# Create your views here.
def model_form_upload(request):
	if request.method == 'POST':
		form = FormularioDocumento(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('exito')
	else:
		form = FormularioDocumento()
	return render(request, 'templates/model_form_upload.html',{
		'form': form
		})


class Exito(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Carga exitosa')