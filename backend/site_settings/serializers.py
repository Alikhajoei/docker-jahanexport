from rest_framework import serializers
from .models import Footer,SocialMediaLink


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['address','address_persian','address_arabic','location_link', 'email', 'phone_number', 'footer_caption', 'footer_caption_arabic','slogan','slogan_persian','slogan_arabic'  ]

class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = ['whatsapp', 'linkedin', 'instagram']
