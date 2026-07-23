from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Link
from .serializers import CreateLinkSerializer, LinkSerializer
from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import filters


# Create your views here.
class CreateLink(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = CreateLinkSerializer


class LinkViewset(ModelViewSet):
    serializer_class = LinkSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["id"]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Link.objects.all()


class RedirectURLView(APIView):
    def get(self, request, code):
        link = get_object_or_404(Link, short_code=code)
        if not link.is_valid():
            return Response({"message": "link is expired or invalid"})
        link.clicks += 1
        link.save()
        return redirect(link.url, permanent=False)
