from typing import List
from django.urls import path
from .views import ListCreateView, ListDeleteView, ListUpdateView, ListPageView, ListDetailView

app_name = "leads"

urlpatterns = [
    path('', ListPageView.as_view(), name='lead-list'),
    path('<int:pk>/', ListDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', ListUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', ListDeleteView.as_view(), name='lead-delete'),
    path('create/', ListCreateView.as_view(), name='lead-create'),
]