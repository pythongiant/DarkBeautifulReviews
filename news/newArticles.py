from rest_framework import serializers
class newsArticleSeralizer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    time = serializers.TimeField();
    content = serializers.CharField()
    image = serializers.ImageField()
    