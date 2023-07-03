from django.urls import path, include

from diploma import views

urlpatterns = [
    path('', views.diploma, name='diploma'),
    path('structure/', views.structure, name='structure'),
    path('techno/', views.techno, name='techno'),
    path('files/', views.files, name='files'),
]