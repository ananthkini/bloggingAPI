from django.conf.urls import url
from django.contrib import admin

from .views import (
    
    post_delete

    )

urlpatterns = [
   
    url(r'^(?P<id>\d+)/delete/$', post_delete, name='deletePost'),
]
