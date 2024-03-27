import uuid
import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser

def generate_unique_id():
    """Generate a unique ID consisting of 24 alphanumeric characters."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(24))

class User(AbstractUser):
    USER_ROLE = 'user'
    ADMIN_ROLE = 'admin'
    DEALER_ROLE = 'dealer'

    ROLE_CHOICES = (
        (USER_ROLE, 'User'),
        (ADMIN_ROLE, 'Admin'),
        (DEALER_ROLE, 'Dealer'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=USER_ROLE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=24, default=generate_unique_id, unique=True)

    def save(self, *args, **kwargs):
        # Set conditions for email, first name, and last name based on role
        if self.role == self.USER_ROLE:
            # Define conditions for users
            pass
        elif self.role == self.ADMIN_ROLE:
            # Define conditions for admins
            pass
        elif self.role == self.DEALER_ROLE:
            # Define conditions for dealers
            pass

        super().save(*args, **kwargs)  # Call the save method of the parent class
