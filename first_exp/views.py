from django.http import HttpResponse
from django.shortcuts import render


database = {
    "pages":[
        {
            "id":1,
            "title":"Page 1",
            "image":"1.png",
            "is_active":True,
            "is_home":True,
            "description":"This is page 1"
        },
        {
            "id":2,
            "title":"Page 2",
            "image":"2.png",
            "is_active":True,
            "is_home":False,
            "description":"This is page 2"
        },
        {
            "id":3,
            "title":"Page 3",
            "image":"3.png",
            "is_active":True,
            "is_home":True,
            "description":"This is page 3"
        }
    ]
}

# Create your views here.
def index(request):
    context = {"pages":database["pages"]}
    return render(request,"first_exp/index.html",context)
def pages(request):
    context = {"pages":database["pages"]}
    return render(request,"first_exp/page_lists.html",context)
def pages_detail(request,id):
    return render(request,"first_exp/pages_detail.html",{"id":id})