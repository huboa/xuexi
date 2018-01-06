from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from django.forms  import widgets
class RegForm(forms.Form):


    username=forms.CharField(min_length=8,error_messages={"required":"该字段不能为空"})
    password=forms.IntegerField(
        widget=widgets.PasswordInput(),
        error_messages = {"invalid": "格式错误，必须输入数字"}
    )
    repeat_password=forms.CharField(
        widget=widgets.PasswordInput(attrs={"egon":1234})
    )
    email=forms.EmailField()


    def clean_username(self):
        if not self.cleaned_data.get("username").isdigit():

            return self.cleaned_data.get("username")
        else:
            raise ValidationError("用户名不能全是数字")


    def clean_password(self):
        if len(str(self.cleaned_data.get("password")))==5:
            return self.cleaned_data.get("password")

        else:
            raise ValidationError("密码必须是5位")


    def clean(self):
        if self.cleaned_data.get("password")==self.cleaned_data.get("repeat_password"):
            return self.cleaned_data

        else:
            raise ValidationError("两次密码不一致")