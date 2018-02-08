from django.shortcuts import render

# def hosts(request):
#     data_list = [
#         {'id':1,'hostname':'c1.com'},
#         {'id':2,'hostname':'c2.com'},
#         {'id':3,'hostname':'c3.com'},
#         {'id':4,'hostname':'c4.com'},
#     ]
#     new_data = []
#     for item in data_list:
#         item['hostname'] = 'bj'+item['hostname']
#         new_data.append(new_data)
#
#     return render(request,'hosts.html',{'data_list':new_data})

def get_new_data(data):
    for item in data:
        item['hostname'] = 'bj' + item['hostname']
        yield item

def hosts(request):
    data_list = [
        {'id':1,'hostname':'c1.com'},
        {'id':2,'hostname':'c2.com'},
        {'id':3,'hostname':'c3.com'},
        {'id':4,'hostname':'c4.com'},
    ]
    # 传递到模板中的是生成器
    new_data = get_new_data(data_list)

    return render(request,'hosts.html',{'new_data':new_data})