from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News
from .newArticles import newsArticleSeralizer

class NewArticles(APIView):
    def get(self,request):
        articles = News.objects.all()
        srl = newsArticleSeralizer(articles,many=True)
        return Response({"articles":srl.data})