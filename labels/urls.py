from django.urls import path
from .views import (
    LabelCreateView,
    LabelListView,
    LabelDetailView,
    LabelUpdateView
)

urlpatterns = [
    path(
        '',
        LabelListView.as_view(),
        name='label_list'),
    path(
        '<int:pk>/',
        LabelDetailView.as_view(),
        name='label_detail'),
    path(
        'add/',
        LabelCreateView.as_view(),
        name='add_label'),
    path(
        'update/<int:pk>/',
        LabelUpdateView.as_view(),
        name='label_update'),
]