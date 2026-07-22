from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("shorten-links", views.LinkViewset, basename="links")

urlpatterns = [
    path("links", views.CreateLink.as_view(), name="create-link"),
] + router.urls
