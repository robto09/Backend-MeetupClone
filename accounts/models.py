from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import random
import string



class MyUserManager(BaseUserManager):

    def create_user(self, username, email, firstname, lastname, activation_token=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('User must a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            activation_token = self.gen_token()
        )
        print('working')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        print(username, email, password)
        user = self.create_user(
            username,
            email,
            password=password,
            firstname='',
            lastname='',
            activation_token=''
        )
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(
        verbose_name='first name',
        max_length=120)
    lastname = models.CharField(
        verbose_name='last name',
        max_length=120)
    profile_image = models.ImageField(upload_to='accounts/images', blank=True, null=True)    
    activation_token = models.CharField(
        verbose_name='activation token',
        max_length=40)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return "{} {}".format(self.firstname, self.lastname)

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
