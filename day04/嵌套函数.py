
def calc(n):
    if n//2 >0:
        calc(n//2)
    print(n)
calc(1024)