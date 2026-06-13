from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import MeView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticação
    path('api/auth/register/',
         include('accounts.urls')),
    path('api/auth/login/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/auth/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/auth/logout/',
         LogoutView.as_view(),
         name='logout'),

    # Usuário logado
    path('api/me/', MeView.as_view(), name='me'),

    # Recurso protegido
    path('api/', include('journal.urls')),
]
