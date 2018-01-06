

from django import forms

from django.forms import widgets


class RegForm(forms.Form):
    username=forms.CharField(min_length=5,
          widget=widgets.TextInput(attrs={"class": "form-control"})
                             )
    password=forms.CharField(min_length=5,
          widget=widgets.TextInput(attrs={"class": "form-control"})
                             )
    repeat_password=forms.CharField(min_length=5,
           widget=widgets.TextInput(attrs={"class": "form-control"})
                                    )
    email=forms.EmailField(min_length=5,
           widget=widgets.TextInput(attrs={"class": "form-control"})
                           )