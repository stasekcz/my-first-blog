
from django.conf.urls import url, include
from django.contrib import admin

# hello

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
