from django.urls import path
from . import views

#url =  htttp://127.0.0.1:8000
urlpatterns = [
    path("",views.index,name="home"),
    path("index",views.index),
    path("pages",views.pages,name="pages"),
    path("pages/<int:id>",views.pages_detail,name="pages_detail")
]
