from django.db import models

# Create your models here.



class Footer(models.Model):
    address = models.CharField(
        verbose_name="آدرس (انگلیسی)", max_length=100, blank=True, null=True
    )
    address_persian = models.CharField(
        verbose_name="آدرس (فارسی)", max_length=100, blank=True, null=True
    )
    address_arabic = models.CharField(
        verbose_name="آدرس (عربی)", max_length=100, blank=True, null=True
    )
    location_link = models.CharField(
        verbose_name="لینک مکان", max_length=128, blank=True, null=True
    )
    footer_caption = models.CharField(
        verbose_name="عنوان فوتر (انگلیسی)", max_length=80, blank=True, null=True
    )
    footer_caption_persian = models.CharField(
        verbose_name="عنوان فوتر (فارسی)", max_length=80, blank=True, null=True
    )
    footer_caption_arabic = models.CharField(
        verbose_name="عنوان فوتر (عربی)", max_length=80, blank=True, null=True
    )
    slogan = models.CharField(
        verbose_name="شعار (انگلیسی)", max_length=60, blank=True, null=True
    )
    slogan_persian = models.CharField(
        verbose_name="شعار (فارسی)", max_length=60, blank=True, null=True   
    )
    slogan_arabic = models.CharField(
        verbose_name="شعار (عربی)", max_length=60, blank=True, null=True
    )
    email = models.CharField(
        verbose_name="ایمیل", max_length=30, blank=True, null=True
    )
    phone_number = models.CharField(
        verbose_name="شماره تلفن", max_length=15, blank=True, null=True
    )
    activate = models.BooleanField(
        verbose_name="فعال‌سازی", default=False
    )

    class Meta:
        verbose_name = "فوتر"
        verbose_name_plural = "فوترها"

    def __str__(self):
        return self.address or "فوتر"

class SiteImage(models.Model):
    name = models.CharField(
        verbose_name="نام", max_length=20
    )
    image = models.ImageField(
        verbose_name="تصویر", upload_to="images/", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تصویر سایت"
        verbose_name_plural = "تصاویر سایت"

class SocialMediaLink(models.Model):
    whatsapp = models.CharField(
        verbose_name="واتساپ", max_length=70, blank=True, null=True
    )
    linkedin = models.CharField(
        verbose_name="لینکدین", max_length=70, blank=True, null=True
    )
    instagram = models.CharField(
        verbose_name="اینستاگرام", max_length=70, blank=True, null=True
    )
    activate = models.BooleanField(
        verbose_name="فعال‌سازی", default=False
    )

    class Meta:
        verbose_name = "لینک شبکه اجتماعی"
        verbose_name_plural = "لینک‌های شبکه اجتماعی"

    def __str__(self):
        return "لینک‌های شبکه اجتماعی"

class SiteVideo(models.Model):
    name = models.CharField(
        verbose_name="نام", max_length=20
    )
    video = models.FileField(
        verbose_name="ویدیو", upload_to="video/", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ویدیو سایت"
        verbose_name_plural = "ویدیوهای سایت"