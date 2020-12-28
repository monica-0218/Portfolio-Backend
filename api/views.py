from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import PostSerializer, SiteDetailSerializer, AbilitySerializer
from .models import Post, SiteDetail, Ability
from django_filters.rest_framework import DjangoFilterBackend


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id',)


class AbilityView(generics.ListAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id',)


class SiteDetailView(generics.ListAPIView):
    queryset = SiteDetail.objects.all()
    serializer_class = SiteDetailSerializer
