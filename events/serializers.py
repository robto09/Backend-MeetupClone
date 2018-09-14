from rest_framework import serializers
from .models import Event, EventCategory, EventReview, EventBooking
from accounts.serializers import UserSerializer

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = (
            'id', 'category', 'image', 'active'
        )

class EventReviewSerializer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField()
    event_detail = serializers.SerializerMethodField()
    class Meta:
        model = EventReview
        fields = (
            'id', 'event', 'rating', 'timestamp', 'user', 'user_detail', 'event_detail',
            'rating', 'review',
        )
    
    def get_user_detail(self, obj):
        return UserSerializer(obj.user).data
    
    def get_event_detail(self, obj):
        return EventSerializer(obj.event).data

class EventSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    category_detail = serializers.SerializerMethodField()
    user_detail = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = (
            'id', 'title', 'about', 'user', 'rating',
             'image', 'category', 
             'reviews', 'timestamp',
            'user_detail', 'category_detail',
             'location', 'event_date', 'ticket_amount_first', 'ticket_amount_second',
             'event_time_start', 'event_time_end', 'chief_guest', 'company_name',
             'company_phone1', 'company_phone2', 'company_email', 'company_address',
             'company_office', 'company_web_address', 'approved'
             )

    def get_reviews(self, obj):
        reviews = EventReview.objects.filter(event=obj)
        a = []
        for x in reviews:
            review = {}
            review['id'] = x.id
            review['username'] = x.user.username
            review['user'] = x.user.id
            review['review'] = x.review
            review['rating'] = x.rating
            review['timestamp'] = x.timestamp
            a.append(review)
        return a

    def get_user_detail(self, obj):
        user_obj = obj.user
        user = UserSerializer(user_obj).data
        return user

    def get_category_detail(self, obj):
        category_obj = obj.category
        category = EventCategorySerializer(category_obj).data
        return category

class EventBookingSerializer(serializers.ModelSerializer):
    event_title = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    class Meta:
        model = EventBooking
        fields =  ['id', 'user', 'username', 'event', 'event_title', 'timestamp', 'quantity']
    
    def get_username(self, obj):
        return obj.user.username
    def get_event_title(self, obj):
        return obj.event.title

class EventBookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventBooking
        fields ='__all__'