from rest_framework import serializers
from news.models import News, Category


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['user', ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        news = News.objects.create(**validated_data)
        return news


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
