from rest_framework import serializers
from .models import ContactUs,ContactUsList


class ContactUsListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    map_image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ContactUsList
        fields = ['title','title_persian','title_arabic','about','about_persian','about_arabic','image_url','map_image_url']
        
        
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None
    
    def get_map_image_url(self, obj):
        if obj.map_image:
            return self.context['request'].build_absolute_uri(obj.map_image.url)
        return None

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'message']
