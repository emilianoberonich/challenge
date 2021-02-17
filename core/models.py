from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Physician(models.Model):
    """Represents an imported physician"""
    class Meta:
        unique_together = ('name_given', 'name_family',)

    name_given = models.CharField(max_length=255, default='', null=True)
    name_family = models.CharField(max_length=255, default='', null=True)
    title = models.CharField(max_length=255, default='', null=True)
    clinic = models.CharField(max_length=255, default='', null=True)

    def __str__(self):
        '''Respresernt a physician as a string'''

        return f'{self.name_given} {self.name_family}'


class UserManager(BaseUserManager):
    """Helps Django work with the user model"""

    def create_user(self, email, password=None, first_name=None, last_name=None):
        """Creates a new user profile object"""

        if not email:
            raise ValueError('Users must have email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    class Meta:
        ordering = ['last_name']

    def create_superuser(self, email, password, first_name=None, last_name=None):
        """Creates and saves a new super with given details"""

        user = self.create_user(email, password, first_name=first_name, last_name=last_name)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Represents a user inside our system"""
    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, default='', null=True)
    last_name = models.CharField(max_length=255, default='', null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """Use to get a user's full name"""

        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """Use to get a user's short name"""

        return self.last_name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email
