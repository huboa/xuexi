from stark.service import v1
from crm import models

class DepartMentConfig(v1.StarkConfig):
    list_display = ['id','title']