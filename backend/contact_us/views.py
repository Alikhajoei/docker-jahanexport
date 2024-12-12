from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  ContactUs,ContactUsList
from .serializers import ContactUsSerializer,ContactUsListSerializer
from site_settings.serializers import FooterSerializer
from site_settings.models import Footer
import os
import json
from django.conf import settings


class ContactUsListView(APIView):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'contact_us', 'data', 'all.json')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                json_data = json.load(json_file)
        except json.JSONDecodeError as e:
            return Response({"error": "Invalid JSON format", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        footer = Footer.objects.filter(activate=True).first()
        footer_data = FooterSerializer(footer, many=False)
        contact_us = ContactUsList.objects.filter(activate=True).first()
        contact_us_data = ContactUsListSerializer(contact_us,context={'request':request})
        footer_data_json= {**footer_data.data,**contact_us_data.data}
        if isinstance(json_data, dict):
            json_data['footer'] = footer_data.data
        elif isinstance(json_data, list):
            json_data.append({'footer': footer_data_json})

        return Response(json_data, status=status.HTTP_200_OK)
    
    
class ContactUsView(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
