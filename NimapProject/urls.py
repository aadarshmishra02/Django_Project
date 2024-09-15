from django.contrib import admin  # Import the admin module
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from DetailApp.views import ClientViewSet, ProjectViewSet, UserProjectView

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'clients/(?P<client_id>[^/.]+)/projects', ProjectViewSet, basename='client-projects')

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line to enable the Django admin
    path('', include(router.urls)),
    path('projects/', UserProjectView.as_view({'get': 'list'})),
]
