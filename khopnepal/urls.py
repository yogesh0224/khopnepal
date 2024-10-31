from django.contrib import admin
from django.urls import path
from khop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('/pregnancyvaccine',views.pregnancyvaccine,name="pregnancyvaciness")
]
