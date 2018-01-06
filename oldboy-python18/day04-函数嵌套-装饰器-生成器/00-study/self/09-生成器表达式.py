with open('a.txt',encoding='utf-8') as f:
    g=(len(line) for line in f)
    print(max(g))

