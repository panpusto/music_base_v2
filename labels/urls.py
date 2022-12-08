from django.urls import path
from .views import LabelCreateView, LabelListView

urlpatterns = [
    path('', LabelListView.as_view(), name='label_list'),
    path('add/', LabelCreateView.as_view(), name='add_label'),
]