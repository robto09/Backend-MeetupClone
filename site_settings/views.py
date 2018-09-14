from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import AddBanner, Cms, GeneralSetting
from .serializers import AddBannerSerializer, CmsSerializer, GeneralSettingSerializer
# Create your views here.

class AddBannerViewSet(viewsets.ModelViewSet):
    permissions_class = [IsAdminUser]
    queryset = AddBanner.objects.all()
    serializer_class = AddBannerSerializer

class CmsViewSet(viewsets.ModelViewSet):
    permissions_class = [IsAdminUser]
    queryset = Cms.objects.all()
    serializer_class = CmsSerializer

class GeneralSettingViewSet(viewsets.ModelViewSet):
    permissions_class = [IsAdminUser]
    queryset = GeneralSetting.objects.all()
    serializer_class = GeneralSettingSerializer