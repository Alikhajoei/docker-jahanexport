from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category,Product
from .serializers import CategoryListSerializer,ProductsSerializer,ProductDetailSerializer

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.filter(parent=None)  
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductsListView(APIView):
    def get(self, request, slug=None):
        try:
            if slug:
                category = Category.objects.get(slug=slug)
                products = category.products.all()  
                serializer = ProductsSerializer(products,context={'request':request} , many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                products = Product.objects.all() 
                serializer = ProductsSerializer(products,context={'request':request} , many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
class ProductDetailView(APIView):
    def get(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            serializer = ProductDetailSerializer(product, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)