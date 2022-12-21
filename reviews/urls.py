from django.urls import path
from reviews.views import ReviewCreateView


urlpatterns = [
    path('add/', ReviewCreateView.as_view(), name='add_review'),
]