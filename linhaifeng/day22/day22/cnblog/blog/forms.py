

from django import forms

from django.forms import widgets

from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class RegForm(forms.Form):
    username=forms.CharField(min_length=5,
          widget=widgets.TextInput(attrs={"class": "form-control"})
                             )
    password=forms.CharField(min_length=5,
          widget=widgets.PasswordInput(attrs={"class": "form-control"})
                             )
    repeat_password=forms.CharField(min_length=5,
           widget=widgets.PasswordInput(attrs={"class": "form-control"})
                                    )
    email=forms.EmailField(min_length=5,
           widget=widgets.TextInput(attrs={"class": "form-control"})
                            )

    def clean_username(self):

        return self.cleaned_data.get("username")

    def clean(self):
        if self.cleaned_data.get("password")==self.cleaned_data.get("repeat_password"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")