from django.urls import path
from . import views

#url =  htttp://127.0.0.1:8000
urlpatterns = [
    path("",views.index),
    path("index",views.index),
    path("pages",views.pages),
    path("another/<int:id>",views.another_detail)
]
