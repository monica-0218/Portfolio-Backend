from rest_framework import serializers
from .models import Post, SiteDetail, Ability


class TagSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return data.values_list('name', flat=True)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializerField()

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(TagSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance

    class Meta:
        model = Post
        fields = '__all__'


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'


class SiteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteDetail
        fields = '__all__'
