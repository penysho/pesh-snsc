from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class SnscUserManager(BaseUserManager):
    """
    下記をもとに、メールアドレスをログイン時に使用するように変更
    https://github.com/django/django/blob/main/django/contrib/auth/models.py#L137
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class SnscUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.

    下記をもとに、メールアドレスをログイン時に使用するように変更
    https://github.com/django/django/blob/main/django/contrib/auth/models.py#L335
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = SnscUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "snsc_user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        # abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Site(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="サイト識別子")
    name = models.CharField(max_length=50, verbose_name="サイト名")
    snsc_users = models.ManyToManyField(SnscUser, through="SiteOwnership")
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "site"
        verbose_name = "サイトマスタ"
        verbose_name_plural = "サイトマスタ"

    def __str__(self):
        return self.name


class SiteOwnership(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    snsc_user = models.ForeignKey(SnscUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "site_ownership"
        verbose_name = "サイト所有権紐付けテーブル"
        verbose_name_plural = "サイト所有権紐付けテーブル"


class Sns(models.Model):
    class SnsName(models.TextChoices):
        INSTAGRAM = "IG", "Instagram"
        TIKTOK = "TK", "TikTok"

    id = models.BigAutoField(primary_key=True, verbose_name="SNS識別子")
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=SnsName, verbose_name="SNS種別")
    username = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="SNSユーザーネーム"
    )
    api_id = token = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="SNS情報取得識別子"
    )
    version = token = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="SNS情報取得バージョン"
    )
    token = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name="SNS情報取得トークン"
    )
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "sns"
        verbose_name = "SNSマスタ"
        verbose_name_plural = "SNSマスタ"

    def __str__(self):
        return self.type


class Post(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="投稿識別子")
    sns = models.OneToOneField(
        Sns,
        on_delete=models.PROTECT,
        primary_key=False,
    )
    site = models.OneToOneField(
        Site,
        on_delete=models.PROTECT,
        primary_key=False,
    )
    username = models.CharField(max_length=50, verbose_name="投稿ユーザーネーム")
    title = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="投稿タイトル"
    )
    like_count = models.IntegerField(blank=True, null=True, verbose_name="投稿いいね数")
    comments_count = models.IntegerField(
        blank=True, null=True, verbose_name="投稿コメント数"
    )
    caption = models.TextField(blank=True, null=True, verbose_name="投稿詳細文")
    permalink = models.URLField(max_length=500, verbose_name="投稿リンク")
    posted_at = models.DateTimeField(verbose_name="投稿日")
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "post"
        verbose_name = "投稿マスタ"
        verbose_name_plural = "投稿マスタ"

    def __str__(self):
        return self.title


class PostMedia(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="投稿メディア識別子")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, verbose_name="投稿メディアタイプ")
    sns_url = models.URLField(
        max_length=1000, blank=True, null=True, verbose_name="SNS側でホストされたURL"
    )
    hosted_list_url = models.FileField(
        upload_to="list/",
        blank=True,
        null=True,
        verbose_name="アプリケーションでホストされた一覧ページ用URL",
    )
    hosted_detail_url = models.FileField(
        upload_to="detail/",
        verbose_name="アプリケーションでホストされた詳細ページ用URL",
    )
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "post_media"
        verbose_name = "投稿メディアマスタ"
        verbose_name_plural = "投稿メディアマスタ"
