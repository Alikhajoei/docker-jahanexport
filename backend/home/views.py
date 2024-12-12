from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HomeController
from .serializers import HomeControllerSerializer
from site_settings.models import Footer, SocialMediaLink
from site_settings.serializers import FooterSerializer, SocialMediaLinkSerializer

class HomeControllerView(APIView):
    def get(self, request):
        home_controllers = HomeController.objects.all()
        home_controllers_data = HomeControllerSerializer(home_controllers,context={'request':request} ,many=True)
        footer = Footer.objects.filter(activate=True).first()
        footer_data = FooterSerializer(footer)
        social_media_links = SocialMediaLink.objects.filter(activate=True).first()
        social_media_links_data = SocialMediaLinkSerializer(social_media_links)

        data = {
            'home_controllers': home_controllers_data.data,
            **footer_data.data,
            **social_media_links_data.data,
        }
        
        if data:
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
