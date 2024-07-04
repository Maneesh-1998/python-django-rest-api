from django.urls import path
from home.views import index,Classperson
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls

urlpatterns = [
    path('index/',index,name='index'),
    path('person/',person,name='person'),
    path('classsperson/',classperson.as_view(),name='classperson'),
    path('',include(router.urls))
]
