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
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="Your API description",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="contact@yourapp.com"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.getProductsApiViewSet.as_view({'get': 'list'}), name="product-list"),
    path('activity/products/<int:pk>/', views.getProductDetailApiViewSet.as_view({'get': 'list'}), name="product-details"),
    path('activity/', views.getActivityApiViewSet.as_view({'get': 'list'}), name="activity-list"),
    path('teacher/', views.getTeacherApiViewSet.as_view({'get': 'list'}), name="teacher-list"),
    path('classroom/', views.getActivityApiViewSet.as_view({'get': 'list'}), name="classroom-list"),

    path('swagger/*.{json,yaml}', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
