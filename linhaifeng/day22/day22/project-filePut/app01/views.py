from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):

    if request.is_ajax():
        print(request.POST)
        print(request.FILES)
        return HttpResponse(123)

    if request.method=="POST":
        print(request.POST)
        print(request.FILES)
        file_obj=request.FILES.get("myFile")
        print(file_obj.name)  #  s6day74.txt

        with open(file_obj.name,"wb") as f:
            for line in file_obj:
                f.write(line)


        return HttpResponse("上传成功")

    return render(request,"index.html")
