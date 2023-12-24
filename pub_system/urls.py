from rest_framework import routers

from pub_system.views import MainViewSet

router = routers.DefaultRouter()

router.register(r'book', MainViewSet, basename='book')
app_name = 'pub_system'
urlpatterns = router.urls

