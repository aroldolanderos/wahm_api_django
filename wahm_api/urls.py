"""wahm_api URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    path('incomes/', include('incomes.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
