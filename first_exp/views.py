from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"first_exp_templates/index.html")
def pages(request):
    return render(request,"first_exp_templates/page_lists.html")
def another_detail(request,id):
    return render(request,"first_exp_templates/another_detail.html",{"id":id})