from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,contact,password=None):
        if not email:
            raise ValueError("User must have email address")
        user = self.model(email =self.normalize_email(email),contact =contact)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,email,contact,password =None):
        user =self.create_user(email,contact,password)
        user.is_admin =True
        user.save(using =self._db)
        return user
    
class CustomUser(AbstractBaseUser): 
    email =models.EmailField(max_length=255,unique=True)
    contact = models.CharField(max_length=15)
    is_active=models.BooleanField(default=True)
    is_admin =models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['contact']

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin