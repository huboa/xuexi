from ..db.models import register_models
def get():
    print('from policy.py')
    register_models('mysql')