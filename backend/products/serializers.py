from rest_framework import serializers
from .models import Category, Product, ProductImage

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title','title_persian','title_arabic','slug')  
        

class CategoryListSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('title','title_persian', 'title_arabic', 'slug', 'subcategories')

    def get_subcategories(self, obj):
        subcategories = obj.categories.all()
        if subcategories.exists():
            return SubCategorySerializer(subcategories, many=True).data
        return []  

class ProductsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('title','title_persian','title_arabic','image_url', 'slug')
        
    def get_image_url(self, obj):
        if obj.main_image:  
            return self.context['request'].build_absolute_uri(obj.main_image.url)  
        return None



class ProductDetailSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    extra_images = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['title','title_persian', 'title_arabic', 'image_url', 'slug', 'caption','caption_persian', 'caption_arabic', 'extra_images']

    def get_image_url(self, obj):
        if obj.main_image:  
            return self.context['request'].build_absolute_uri(obj.main_image.url)  
        return None

    def get_extra_images(self, obj):
        images = obj.extra_images.all()
        return [self.context['request'].build_absolute_uri(image.image.url) for image in images]

