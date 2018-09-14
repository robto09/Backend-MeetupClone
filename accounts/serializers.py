from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import MyUser
from events.models import EventReview
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import string, random
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    def gen_token(self):
        choices = string.ascii_letters + string.digits + string.hexdigits
        gen = ''
        for i in range(40):
            gen += random.choice(choices)
        return gen
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = MyUser
        fields = (
            'id', 'email', 'username', 'firstname', 'lastname', 'profile_image',
            'is_admin', 'reviews', 'is_active', 'password'
        )
        read_only_fields = ('last_login','activation_token', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_reviews(self, obj):
        reviews = []
        reviews_qs = EventReview.objects.filter(user=obj.id)
        for review in reviews_qs:
            a = {}
            a['id'] = review.id
            a['event_id'] = review.event.id
            a['rating'] = review.rating
            a['review'] = review.review
            reviews.append(a)
        return reviews

    def create(self, validated_data, *args, **kwargs):
        user = MyUser(
            username = validated_data['username'],
            email = validated_data['email'],
            firstname = validated_data['firstname'],
            lastname = validated_data['lastname'],
            activation_token = self.gen_token(),
            is_admin = validated_data['is_admin']
        )
        user.set_password(validated_data['password'])
        user.save()
        if(user):
            current_site = 'localhost:8000'
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user.username,
                'domain': current_site,
                'token':user.activation_token,
            })
            to_email = user.email
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()
    class Meta:
        fields = [
            'username',
            'password',
            'email',
            'token',
            'id',
            'is_active',
            'is_admin',
        ]
        model = MyUser
        extra_kwargs = {
            "password": {"write_only": True}, 
            "email": {"read_only": True},
            "is_active": {"read_only": True},  
            "is_admin": {"read_only": True},  
            "id": {"read_only": True},  
        }

    def validate(self, data):
        username = data.get('username', None)
        password = data['password']
        if not username:
            raise ValidationError('A username is required to login')
        user = MyUser.objects.get(username=username)
        if not user:
            raise ValidationError('the username is not valid')
        if(user):
            if not user.check_password(password):
                raise ValidationError('Incorrect Credential please try again')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        data['token'] = token
        data['id'] = user.id
        return data

