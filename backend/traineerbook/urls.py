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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openapi.yaml', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/products/', views.getProductsApiViewSet.as_view({'get': 'list'}), name="product-list"),
    path('api/activity/products/<int:pk>/', views.getProductDetailApiViewSet.as_view({'get': 'list'}), name="product-details"),
    path('api/activity/', views.getActivityApiViewSet.as_view({'get': 'list'}), name="activity-list"),
    path('api/auth/register/', views.RegisterUserView.as_view(), name='register'),
    path('api/auth/login/', views.LoginView.as_view(), name='login'),
    path('api/auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/auth/me/', views.CurrentUserView.as_view(), name='current_user'),
    path('api/comment/create/', views.CreateComentView.as_view(), name='create_comment'),
    path('api/comment/<int:pk>/', views.GetCommentListApiViewSet.as_view({'get': 'list'}), name='comment_list'),
    path('api/cart/', views.ShoppingCartGetView.as_view(), name='get_cart'),
    path('api/cart/add/<int:product_id>/<int:quantity>/', views.ShoppingCartPutView.as_view(), name='add_to_cart'),
    path('api/cart/remove/<int:product_id>/', views.ShoppingCartDeleteView.as_view(), name='remove_from_cart'),
]
