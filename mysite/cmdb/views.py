from django.http import HttpResponse
from django.shortcuts import render

# user_list = [
#     {"user": "jack", "pwd": "abc"},
#     {"user": "tom", "pwd": "ABC"},
# ]


# Create your views here.
from cmdb import models


def index(request):
    # return HttpResponse("Hello World")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print(username, password)
        # temp = {"user": username, "pwd": password}
        # user_list.append(temp)

        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})
