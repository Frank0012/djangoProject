from django.contrib import admin
from django.urls import include, path
from . import contactForm
from . import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', index.index, name='index'),
    path('contact/', contactForm.contact, name = 'contact')
]
