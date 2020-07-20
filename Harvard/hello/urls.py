from  django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="hello/index.html"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet")

]