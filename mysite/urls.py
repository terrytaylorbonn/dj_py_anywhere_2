"""
URL configuration for mysite project.

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
from django.urls import path, include, re_path
from django.contrib.auth import views 

#from drf-yasg import openapi
#from drf-yasg.views import get_schema_view as swagger_get_schema_view
# schema_view = swagger_get_schema_view(
#     openapi.Info(
#         title="Posts API",
#         default_version='1.0.0',
#         description="API documentation of App",
#     ),
#     public=True,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', views.LoginView.as_view(), name='login'),
    path('accounts/', views.LogoutView.as_view(), name='logout'),
    path('api/v1/', 
        include([
            path('post/', include(('post.api.urls', 'post'), namespace='posts')),
           # path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
            # path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
        ])
    ),
    path('api/', include('api.urls')),
    # Other routes
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
