from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quickstart/', include('quickstart.urls')),
    path('quickstart/token/', TokenObtainPairView.as_view(), name='got_token'),
    path('quickstart/token/refresh', TokenRefreshView.as_view(), name='refresh'),


]
