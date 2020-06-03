from django.urls import path
from . import views

urlpatterns = [
   path('about/', views.about, name='about'),
   path('blog/', views.post_list, name='post-list'),
   path('CV/', views.CV, name='CV'),
   path('projects/', views.projects, name='projects')
]

