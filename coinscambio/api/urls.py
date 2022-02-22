from rest_framework import routers
from api.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
urlpatterns = router.urls
