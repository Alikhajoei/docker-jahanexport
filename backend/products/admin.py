from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = Product.extra_images.through
    extra = 1
    
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'title_arabic', 'parent')
    search_fields = ('title' , 'title_arabic','parent')
    exclude = ('slug',)
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title' ,'title_arabic', 'category')
    search_fields = ('title' ,'title_arabic','category__title' ,'category__title_arabic')
    list_filter = ('category',)
    inlines = [ProductImageInline]
    exclude = ('extra_images','slug')
    
    
    
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    
    
