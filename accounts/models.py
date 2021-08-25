from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("학교 이메일", unique=True, blank=False)
    nickname = models.CharField("닉네임", max_length=30, blank=True)
    is_staff = models.BooleanField("스태프 권한", default=False)
    is_active = models.BooleanField(_("active"), default=False)
    date_joined = models.DateTimeField("가입일", default=timezone.now)
    subjects = models.ManyToManyField(
        "Subjects", related_name="subjects", null=True, blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"  # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ["nickname"]  # 필수입력값

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        swappable = "AUTH_USER_MODEL"

    def email_user(self, subject, message, from_email=None, **kwargs):  # 이메일 발송 메소드
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Subjects(models.Model):

    """Major Model"""

    TRACK_LANGUAGE = "language & ai"
    TRACK_SOFTWARE = "software & ai"
    TRACK_BUSINESS = "business & ai"
    TRACK_COMMON = "common"

    TRACK_CHOICES = (
        (TRACK_LANGUAGE, "Language & AI"),
        (TRACK_SOFTWARE, "Software & AI"),
        (TRACK_BUSINESS, "Business & AI"),
        (TRACK_COMMON, "Common"),
    )

    SEMESTER_FIRST = "first semester"
    SEMESTER_SECOND = "second semester"

    SEMESTER_CHOICES = (
        (SEMESTER_FIRST, "First"),
        (SEMESTER_SECOND, "Second"),
    )

    name = models.CharField(max_length=30)
    require = models.BooleanField()
    year = models.IntegerField()
    credit = models.IntegerField()
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=6, blank=True)
    track = models.CharField(choices=TRACK_CHOICES, max_length=20, blank=True)

    def __str__(self):
        return self.name
