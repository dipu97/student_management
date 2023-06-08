from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, hod_views, staff_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.home, name='home'),
    path('', views.login, name='login')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
