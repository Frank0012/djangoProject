from django.contrib import admin
from django.urls import include, path
from . import contactForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('contact/', contactForm.contact, name = 'contact')
]
