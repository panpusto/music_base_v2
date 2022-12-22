from django.urls import path
from reviews.views import ReviewCreateView, ReviewListView, ReviewDetailView


urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('add/', ReviewCreateView.as_view(), name='add_review'),
]
