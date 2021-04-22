from django.urls import path
from vlog import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('vlog/', views.VlogList.as_view()),
    path('vlogs/<int:pk>/', views.VlogDetail.as_view()),
]

urlpatterns= format_suffix_patterns(urlpatterns)