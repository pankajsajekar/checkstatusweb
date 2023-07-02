from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
