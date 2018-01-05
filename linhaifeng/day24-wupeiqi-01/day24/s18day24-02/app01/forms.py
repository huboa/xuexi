from django.forms import Form
from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets as fwidgets

class LoginForm(Form):
    username = fields.CharField(
        label='用户名',
        required=True,
        error_messages={
            'required':'用户名不能为空'
        },
        widget=fwidgets.TextInput(attrs={'class':'form-control'})
    )
    password = fields.CharField(
        label='密码',
        required=True,
        error_messages={
            'required': '密码不能为空'
        },
        widget=fwidgets.PasswordInput(attrs={'class':'form-control'})
    )


from app01 import models
class HostModelForm(ModelForm):
    # xxx = fields.CharField()

    class Meta:
        model = models.Host
        fields = "__all__"
        # fields = ['hostname','ip']
        labels = {
            'ip':'IP',
            'port':'端口',
        }
        error_messages = {
            'hostname':{
                'required':'主机名不能为空.',
            },
            'ip': {
                'required': 'IP不能为空.',
            },
        }
        widgets = {
            'hostname': fwidgets.Textarea(attrs={'class':'c1'})
        }

    def clean_hostname(self):
        from django.core.exceptions import ValidationError
        hostname = self.cleaned_data['hostname']
        if len(hostname) > 6:
            raise ValidationError('主机名已存在')
        return hostname