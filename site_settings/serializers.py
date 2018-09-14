from rest_framework import serializers
from .models import AddBanner, Cms, GeneralSetting

class AddBannerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AddBanner

class CmsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Cms

class GeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = GeneralSetting