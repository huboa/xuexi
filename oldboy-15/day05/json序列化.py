import json
data = {"name":"zsc",
        "age":18,
        "sex":"M"}

f =open("data.txt","w",encoding="utf-8")
f.write(json.dumps(data))
f.close()
f=open("data.txt","r")
t=json.load(f)
t1=json.loads(f.read())
print(t1)
for n in t:
    print(n)