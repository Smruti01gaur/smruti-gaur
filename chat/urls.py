from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, MessageViewSet


router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('messages', MessageViewSet, basename='messages')

urlpatterns = router.urls