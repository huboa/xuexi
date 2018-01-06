from django.shortcuts import render,HttpResponse

# Create your views here.



def article_year(request,year):


    # select * from Ariticle  where year=year

    return HttpResponse(str(year))



def article_yearMonth(request,month_id,year_id):


    return HttpResponse("OK"+year_id+month_id)


def test(q):

    return HttpResponse("test2003")

