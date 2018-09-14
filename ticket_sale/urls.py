"""ticket_sale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from accounts.views import (
    ActivateView, 
    UserLoginAPIView, 
    ForgotPassword,
)
from events.views import (
    EventViewSet,
    EventCategoryViewSet,
    EventReviewViewSet,
    EventBookingViewSet,
    EventBookingCreate,
    ApproveEvent,
    ActivateCategory
)
from site_settings.views import (
    AddBannerViewSet, 
    CmsViewSet,
    GeneralSettingViewSet
)
from accounts.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'events', EventViewSet, base_name='events')
router.register(r'event-category', EventCategoryViewSet, base_name='event-category')
router.register(r'event-review', EventReviewViewSet, base_name='event-review')
router.register(r'event-booking', EventBookingViewSet, base_name='event-booking')
router.register(r'add-banner', AddBannerViewSet, base_name='add-banner')
router.register(r'cms', CmsViewSet, base_name='cms')
router.register(r'general-settings', GeneralSettingViewSet, base_name='general-settings')

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/category/activate/', ActivateCategory.as_view() ),
    path('api/event/approve/', ApproveEvent.as_view() ),
    path('api/account/reset-password/', ForgotPassword.as_view() ),
    path('api/account/login/', UserLoginAPIView.as_view() ),
    path('api-token-auth/', obtain_jwt_token),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += re_path('.*', TemplateView.as_view(template_name='index.html')),
    