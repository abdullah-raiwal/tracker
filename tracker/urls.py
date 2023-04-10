
from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('expenseApp.api.urls')),
    path('api/account/', include('accounts_app.api.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', views.hello_world)
]
