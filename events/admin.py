from django.contrib import admin
from .models import Event, EventCategory, EventReview, EventBooking
# Register your models here.

admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(EventBooking)
admin.site.register(EventReview)
