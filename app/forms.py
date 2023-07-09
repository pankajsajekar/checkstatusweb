from django import forms
from . import models
from django.forms import TextInput, DateField

class CertificateForm(forms.Form):
    serialno = forms.CharField(max_length=250, required=True)
    issuingdate = forms.DateField(required=True)
    validtill = forms.DateField(required=True)


class CheckCertForm(forms.Form):
    serialno = forms.CharField(max_length=250, required=True)
