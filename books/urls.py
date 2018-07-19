from django.conf.urls import include, url
from books.views import contact

urlpatterns = [
    url('contact/',contact)
]