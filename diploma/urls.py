from django.urls import path, include

from diploma import views

urlpatterns = [
    path('structure/', views.structure, name='structure'),
    path('techno/', views.techno, name='techno'),
    path('files/', views.files, name='files'),
]