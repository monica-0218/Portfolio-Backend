from django.urls import path
from .views import PostView, SiteDetailView, AbilityView

urlpatterns = [
    path('post/', PostView.as_view()),
    path('site/', SiteDetailView.as_view()),
    path('ability/', AbilityView.as_view()),
]
