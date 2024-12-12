from django.db import models

# Create your models here.


class ContactUsList(models.Model):
    title = models.CharField(
        verbose_name="عنوان (انگلیسی)", max_length=100, blank=True, null=True
    )
    title_persian = models.CharField(
        verbose_name="عنوان (فارسی)", max_length=100, blank=True, null=True
    )
    title_arabic = models.CharField(
        verbose_name="عنوان (عربی)", max_length=100, blank=True, null=True
    )
    about = models.CharField(
        verbose_name="درباره (انگلیسی)", max_length=1000, blank=True, null=True
    )
    about_persian = models.CharField(
        verbose_name="درباره (فارسی)", max_length=1000, blank=True, null=True
    )
    about_arabic = models.CharField(
        verbose_name="درباره (عربی)", max_length=1000, blank=True, null=True
    )
    image = models.ImageField(
        verbose_name="تصویر", upload_to="images/contatus/"
    )
    map_image = models.ImageField(
        verbose_name="تصویر نقشه", upload_to="images/contatus/map/"
    )
    activate = models.BooleanField(
        verbose_name="فعال‌سازی", default=False
    )

    class Meta:
        verbose_name = "لیست تماس با ما"
        verbose_name_plural = "لیست‌های تماس با ما"

    def __str__(self) -> str:
        return "فعال" if self.activate else "غیرفعال"



class ContactUs(models.Model):
    first_name = models.CharField(
        verbose_name="نام", max_length=50
    )
    last_name = models.CharField(
        verbose_name="نام خانوادگی", max_length=50
    )
    email_address = models.EmailField(
        verbose_name="آدرس ایمیل"
    )
    phone_number = models.CharField(
        verbose_name="شماره تلفن", max_length=20
    )
    message = models.TextField(
        verbose_name="پیام"
    )
    is_read = models.BooleanField(
        verbose_name="خوانده شده", default=False
    )

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "پیام‌های تماس با ما"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
