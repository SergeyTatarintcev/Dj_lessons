from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),

    path('login/',  auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cabinet/', main_views.cabinet, name='cabinet'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
