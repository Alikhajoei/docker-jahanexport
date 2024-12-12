from typing import Iterable
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify



class Category(models.Model):
    title = models.CharField(
        verbose_name="عنوان (انگلیسی)", max_length=100
    )
    title_persian = models.CharField(
        verbose_name="عنوان (فارسی)", max_length=100, blank=True, null=True
    )
    title_arabic = models.CharField(
        verbose_name="عنوان (عربی)", max_length=100
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='categories',
        on_delete=models.CASCADE,
        verbose_name="دسته‌بندی والد"
    )
    slug = models.SlugField(
        unique=True, blank=True, verbose_name="نامک"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="دسته‌بندی"
    )
    title = models.CharField(
        verbose_name="عنوان (انگلیسی)", max_length=100
    )
    title_persian = models.CharField(
        verbose_name="عنوان (فارسی)", max_length=100, blank=True, null=True
    )
    title_arabic = models.CharField(
        verbose_name="عنوان (عربی)", max_length=100
    )
    main_image = models.ImageField(
        verbose_name="تصویر اصلی", upload_to="products/main/"
    )
    extra_images = models.ManyToManyField(
        'ProductImage',
        related_name="products",
        blank=True,
        verbose_name="تصاویر اضافی"
    )
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name="متن نمایشی (انگلیسی)")
    description_persian = models.CharField(max_length=200, blank=True, null=True, verbose_name="متن نمایشی (فارسی)")
    description_arabic = models.CharField(max_length=200, blank=True, null=True,verbose_name="متن نمایشی (عربی)")
    
    caption = RichTextField(
        verbose_name="توضیحات (انگلیسی)", blank=True, null=True
    )
    caption_persian = RichTextField(
        verbose_name="توضیحات (فارسی)", blank=True, null=True
    )
    caption_arabic = RichTextField(
        verbose_name="توضیحات (عربی)", blank=True, null=True
    )
    slug = models.SlugField(
        max_length=100, blank=True, null=True, unique=True,
        verbose_name="نامک"
    )
    created_at = models.DateTimeField(
        verbose_name="تاریخ ایجاد", auto_now_add=True
    )

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class ProductImage(models.Model):
    image = models.ImageField(
        verbose_name="تصویر", upload_to="products/extra/"
    )

    def __str__(self):
        return "تصویر اضافی محصول"

    class Meta:
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصولات"