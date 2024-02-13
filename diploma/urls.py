from django.urls import path, include

from diploma import views

urlpatterns = [
    path('', views.diploma, name='diploma'),
    path('structure/', views.structure, name='structure'),
    path('structure-mobile/', views.structure_mobile, name='structure_mobile'),
    path('techno/', views.techno, name='techno'),
    path('techno-mobile/', views.techno_mobile, name='techno_mobile'),
    path('files/', views.files, name='files'),
    path('files-mobile/', views.files_mobile, name='files_mobile'),
]