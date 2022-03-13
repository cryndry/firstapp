from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"first_exp/index.html")
def pages(request):
    return render(request,"first_exp/page_lists.html")
def pages_detail(request,id):
    return render(request,"first_exp/pages_detail.html",{"id":id})