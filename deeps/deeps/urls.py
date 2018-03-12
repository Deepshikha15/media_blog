
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('cl.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^cl/', include('cl.urls')),
]
