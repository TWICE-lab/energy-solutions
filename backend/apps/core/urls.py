from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, ServiceViewSet, ProjectViewSet,
    ContactMessageViewSet, TeamMemberViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contact', ContactMessageViewSet)
router.register(r'team', TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
