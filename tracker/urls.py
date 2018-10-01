from django.urls import path
from .views import (
    UsersRunListView,
    RunDetailView,
    RunCreateView,
    RunUpdateView,
    RunDeleteView,
)
from . import views

# urlpatterns = [
#     path('', views.index),
#     path('home/', views.UsersRunListView.as_view(), name='user-run-list')
# ]

urlpatterns = [
    path('', UsersRunListView.as_view(), name='users-run'),
    #path('run/user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('run/<int:pk>/', RunDetailView.as_view(), name='run-detail'),
    path('run/new/', RunCreateView.as_view(), name='run-create'),
    path('run/<int:pk>/update/', RunUpdateView.as_view(), name='run-update'),
    path('run/<int:pk>/delete/', RunDeleteView.as_view(), name='run-delete'),
]
