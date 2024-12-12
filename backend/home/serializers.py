from rest_framework import serializers
from .models import SliderImages, HomeController, FestivalSale
from products.models import Product
from site_settings.serializers import FooterSerializer, SocialMediaLinkSerializer


class SliderImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = SliderImages
        fields = [ 'text','text_persian','text_arabic', 'button_text', 'has_button','button_text_persian','button_text_arabic', 'navigate_to', 'image_url']

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'image'):
            return self.context['request'].build_absolute_uri(obj.image.image.url)
        return None
    
class LatestProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'title','title_persian', 'title_arabic', 'description','description_persian','description_arabic','slug', 'image_url']
        
    def get_image_url(self, obj):
        if obj.main_image:  
            return self.context['request'].build_absolute_uri(obj.main_image.url)  
        return None

        
class FestivalSaleSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = FestivalSale
        fields = [ 'title','title_persian', 'title_arabic', 'caption', 'caption_persian','caption_arabic', 'discount', 'image', 'image_url', 'activate']

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'image'):
            return self.context['request'].build_absolute_uri(obj.image.image.url)
        return None

class HomeControllerSerializer(serializers.ModelSerializer):
    slider_data = SliderImagesSerializer(many=True)
    video_url = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    sale_festivals = serializers.SerializerMethodField()

    class Meta:
        model = HomeController
        fields = [ 'slider_data',  'video_url', 'activate','products','sale_festivals' ]

    def get_video_url(self, obj):
        if obj.video_trailer and hasattr(obj.video_trailer, 'video'):  
            return self.context['request'].build_absolute_uri(obj.video_trailer.video.url)  
        return None
    
    def get_products(self, obj):
        products = Product.objects.order_by('-created_at')[:10]
        if products:
            return LatestProductSerializer(products, many=True, context=self.context).data
        return None

    def get_sale_festivals(self, obj):
        sale_festivals = FestivalSale.objects.filter(activate=True).first()
        if sale_festivals:
            return FestivalSaleSerializer(sale_festivals, context=self.context).data
        return None
