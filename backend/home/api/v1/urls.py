from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NewModel1ViewSet,ProductViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('product', ProductViewSet )
router.register('newmodel1', NewModel1ViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
