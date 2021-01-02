from django.conf.urls import url

from . import views

app_name='handwritten'

urlpatterns = [
    url('home/', views.convert, name='convert'),
]