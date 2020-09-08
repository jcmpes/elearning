from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from register import views as v

urlpatterns = [
    path('', include('courses.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # path('courses/', include('courses.urls', namespace='courses')),
    path('memberships/', include('memberships.urls', namespace='memberships')),
    path("register/", v.register, name="register"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)