def func(ff):
    try:
        ff=int(ff)
        return isinstance(ff,int)
    except ValueError:
        return False

ss="-242.99999999999997"
print(func(ss))