from django.shortcuts import render

# Create your views here.
def gestion_documento(request):
    return render(request, 'gestion_documento.html')

