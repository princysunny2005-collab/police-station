from django import forms

from . models import ComplaintReg

class ComplaintRegForms(forms.ModelForm):

    class Meta:
        model = ComplaintReg
        fields = "__all__"