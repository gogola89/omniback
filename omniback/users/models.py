from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from omniback.users.managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for omniback.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    first_name = models.CharField(_("User's first name"), max_length=20, blank=True, null=True)
    last_name = models.CharField(_("User's last name"), max_length=20, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(_("Your unique username"), unique=True, max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(
        _("User profile image"),
        upload_to="userprofile",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.email

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
