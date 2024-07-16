from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Assuming you're using django-allauth
    path('', include('vehicles.urls')),  # Include your app's URLs here
]

