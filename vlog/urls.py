from django.urls import path
from vlog import views

urlpatterns = [
    path('vlog/', views.vlog_list),
    path('vlogs/<int:pk>/', views.vlog_detail),
]