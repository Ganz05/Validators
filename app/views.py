from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def add_animal(request):
    ELAO=AnimalForm()
    d={'ELAO':ELAO}
    if request.method=='POST':
        CLAO=AnimalForm(request.POST)
        if CLAO.is_valid():
            na=CLAO.cleaned_data['name']
            zo=CLAO.cleaned_data['zoo']
            id=CLAO.cleaned_data['aid']
            re=CLAO.cleaned_data['re_enter']
            NAO=Animal.objects.get_or_create(name=na,zoo=zo,aid=id,re_enter=re)[0]
            NAO.save()
            return HttpResponse('Data Inserted Succussfully')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'add_animal.html',d)
