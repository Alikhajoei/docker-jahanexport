from django.shortcuts import render
from .models import Footer,SocialMediaLink
from .serializers import FooterSerializer, SocialMediaLinkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class FooterView(APIView):
    def get(self, request):
        footer = Footer.objects.filter(activate=True).first()
        footer_data = FooterSerializer(footer, many=False)
        social_media_links = SocialMediaLink.objects.filter(activate = True).first()
        social_media_links_data = SocialMediaLinkSerializer(social_media_links,many=False)
        combined_data = {**footer_data.data, **social_media_links_data.data}
        return Response(combined_data, status=status.HTTP_200_OK)