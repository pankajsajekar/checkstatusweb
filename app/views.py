from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import CertificateForm, CheckCertForm
from .models import CertificateModel

class home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        context ={}

        # create object of form
        form = CheckCertForm(request.POST or None)
        
        if form.is_valid():

            serialno = request.POST.get('serialno')
            print(serialno)
            if serialno:
                obj = CertificateModel.objects.filter(serialno = serialno)
                print(obj)
                if obj:
                    for i in obj:
                        obj1 = i
                    context = {'certificateObj': obj1, 'certifacate': True}
                    return render(request, "showCert.html", context)
                else:
                    context = {"error": "serial no. wrong", 'certifacate': False}
                
                context = {"error": "serial no. wrong", 'certifacate': False}
                return render(request, "index.html", context)
    
        # context['form']= form
        context = {"form": form, 'certifacate': False}
        # return HttpResponse('POST request!')
        return render(request, "index.html", context)


class AddCertficateView(View):
    def get(self, request, *args, **kwargs):
        form = CertificateForm(request.POST or None)
        context = {"form": form}
        return render(request, 'addCert.html', context)

    def post(self, request, *args, **kwargs):
        form = CertificateForm(request.POST or None)
        if form.is_valid:
            serialno = request.POST.get('serialno')
            issuingdate = request.POST.get('issuingdate')
            validtill = request.POST.get('validtill')
            obj = CertificateModel.objects.create(serialno=serialno, issuingdate=issuingdate,validtill=validtill)
            obj.save()
            context = {"AddcertSuccessful": True}
            return render(request, "index.html", context)
        context = {"form": form}
        return render(request, 'addCert.html', context)
        