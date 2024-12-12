from django.db import models
from site_settings.models import SiteImage ,SiteVideo
from django.core.validators import MaxValueValidator

# Create your models here.

class SliderImages(models.Model):
    text = models.CharField(
        verbose_name="متن (انگلیسی)", max_length=128, blank=True, null=True
    )
    text_persian = models.CharField(
        verbose_name="متن (فارسی)", max_length=128, blank=True, null=True
    )
    text_arabic = models.CharField(
        verbose_name="متن (عربی)", max_length=128, blank=True, null=True
    )
    image = models.ForeignKey(
        SiteImage, 
        on_delete=models.PROTECT, 
        related_name="images", 
        verbose_name="تصویر"
    )
    button_text = models.CharField(
        verbose_name="متن دکمه (انگلیسی)", max_length=20, blank=True, null=True
    )
    button_text_persian = models.CharField(
        verbose_name="متن دکمه (فارسی)", max_length=20, blank=True, null=True
    )
    button_text_arabic = models.CharField(
        verbose_name="متن دکمه (عربی)", max_length=20, blank=True, null=True
    )
    navigate_to = models.CharField(
        verbose_name="لینک مسیر", max_length=20, blank=True, null=True
    )

    def has_button(self):
        return bool(self.navigate_to)

    class Meta:
        verbose_name = "تصویر اسلایدر"
        verbose_name_plural = "تصاویر اسلایدر"

    def __str__(self):
        return self.text or "اسلایدر بدون متن"

class HomeController(models.Model):    
    slider_data = models.ManyToManyField(
        SliderImages, 
        related_name="home_controllers", 
        verbose_name="داده‌های اسلایدر"
    )
    video_trailer = models.ForeignKey(
        SiteVideo, 
        on_delete=models.PROTECT, 
        related_name="home_controllers", 
        blank=True, 
        null=True, 
        verbose_name="ویدیو تریلر"
    )
    activate = models.BooleanField(
        verbose_name="فعال‌سازی", default=False
    )

    class Meta:
        verbose_name = "کنترلر صفحه اصلی"
        verbose_name_plural = "کنترلرهای صفحه اصلی"

    def __str__(self):
        return "فعال" if self.activate else "غیرفعال"

class FestivalSale(models.Model):
    title = models.CharField(
        verbose_name="عنوان (انگلیسی)", max_length=20
    )
    title_persian = models.CharField(
        verbose_name="عنوان (فارسی)", max_length=20
    )
    title_arabic = models.CharField(
        verbose_name="عنوان (عربی)", max_length=20
    )
    caption = models.CharField(
        verbose_name="توضیحات (انگلیسی)", max_length=128
    )
    caption_persian = models.CharField(
        verbose_name="توضیحات (فارسی)", max_length=128
    )
    caption_arabic = models.CharField(
        verbose_name="توضیحات (عربی)", max_length=128
    )
    discount = models.PositiveSmallIntegerField(
        verbose_name="تخفیف", 
        null=True, 
        blank=True, 
        validators=[MaxValueValidator(100)]
    )
    image = models.ImageField(
        verbose_name="تصویر جشنواره", upload_to="image_festival/"
    )
    activate = models.BooleanField(
        verbose_name="فعال‌سازی", default=False
    )

    class Meta:
        verbose_name = "جشنواره فروش"
        verbose_name_plural = "جشنواره‌های فروش"

    def __str__(self):
        return self.title