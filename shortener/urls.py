from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("api/shorten-links", views.LinkViewset, basename="links")

urlpatterns = [
    path("api/links", views.CreateLink.as_view(), name="create-link"),
    path("<str:code>/", views.RedirectURLView.as_view(), name="redirect-link"),
] + router.urls
