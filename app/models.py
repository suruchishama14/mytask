from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, class_1, section, subject, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email is not valid')

        email = self.normalize_email(email)
        user = self.model(email=email, class_1=class_1, section=section, subject=subject, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, class_1, section, subject, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, class_1, section, subject, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, class_1, section, subject, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, class_1, section, subject, first_name, last_name, password, **extra_fields)


SECTION_CHOICE = (
    ("A", 'A'),
    ("B", 'B'),
    ("C", 'C'),
)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    class_1 = models.CharField(max_length=15, verbose_name='Class', blank=True)
    section = models.CharField(max_length=8, choices=SECTION_CHOICE, verbose_name='Section', blank=True)
    subject = models.CharField(max_length=15, verbose_name='Subject', blank=True)
    first_name = models.CharField(max_length=150, verbose_name='First Name')
    last_name = models.CharField(max_length=150, verbose_name='Last Name')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'class_1', 'section', 'subject']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    objects = CustomUserManager()

class TecherModel(models.Model):
    username = models.CharField(unique=True,max_length=30)
    password = models.CharField(max_length=30)


class Timetable(models.Model):
    name=models.CharField(max_length=30)
    date = models.DateField()
    time=models.TimeField()
    subject=models.CharField(max_length=50)