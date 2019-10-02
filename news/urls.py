from django.urls import include,path
from django.conf.urls import url,include
from rest_framework import routers,serializers,viewsets
from .views import NewArticles
urlpatterns = [
    path("api/",NewArticles.as_view())
]
