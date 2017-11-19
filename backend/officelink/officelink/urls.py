from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from camera.views import RoomViewSet, CameraViewSet, RoomHighestOccurenceView, MeasurementCreateView


router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'cameras', CameraViewSet)
router.register(r'measurement', MeasurementCreateView)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/rooms/best', RoomHighestOccurenceView.as_view()),
    url(r'^admin/', admin.site.urls),
]
