from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manage user profiles"""

    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('User Must have an email address')
        
        email = self.normalize_email(email)
        """making a user model with the two parameters"""
        user  = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db) 

        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff     = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get full name from the database"""
        return self.name
    
    def get_short_name(self):
        """Get the short name from the user"""
        return self.name

    def __str__(self):
        """String representation of the user"""
        return self.email
