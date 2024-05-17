from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Task', TaskView, basename='task')

urlpatterns = router.urls