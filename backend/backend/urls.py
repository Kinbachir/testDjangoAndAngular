from django.urls import path, include
from rest_framework import routers
from .views import DocumentViewSet, AnnotationViewSet

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'annotations', AnnotationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]