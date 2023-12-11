from django.urls import path
from TraineerbookApp import views

"""
URL configuration for traineerbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.getProductsApiViewSet.as_view({'get': 'list'}), name="product-list"),
    path('activity/products/<int:pk>/', views.getProductDetailApiViewSet.as_view({'get': 'list'}), name="product-details"),
    path('activity/', views.getActivityApiViewSet.as_view({'get': 'list'}), name="activity-list"),
    path('openapi.yaml', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('auth/register/', views.RegisterUserView.as_view(), name='register'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/me/', views.CurrentUserView.as_view(), name='current_user'),
    path('comment/create/', views.CreateComentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/', views.GetCommentListApiViewSet.as_view({'get': 'list'}), name='comment_list'),
    path('incident/<int:pk>/', views.GetIncidentApiViewSet.as_view(), name='incident_id'),
    path('incident/user', views.GetUserIncidentApiViewSet.as_view(), name='incident_user'),
    path('incident/create', views.IncidentCreateApiViewSet.as_view(), name='incident_create'),
]
