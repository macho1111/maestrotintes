from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Prefecture(models.Model):
    name = models.CharField(max_length=100, verbose_name='都道府県')
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='送料', default=0)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('ユーザー登録にはEメールが必要です。')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Eメールアドレス',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255, verbose_name='名前', blank=True, null=True)
    furigana = models.CharField(max_length=255, verbose_name='フリガナ', blank=True, null=True)
    prefecture = models.ForeignKey(Prefecture, verbose_name='都道府県', on_delete=models.SET_NULL, blank=True, null=True, related_name='users')
    address = models.CharField(max_length=255, verbose_name='住所', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='電話番号', blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False) 
   
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):             
        return self.email

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active