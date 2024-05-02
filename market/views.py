from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework import status

from market.models import Product
from market.serializers import ProductSerializer, ProductListSerializer, UpdateProductStockSerializer
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class APIRoot(APIView):
    def get(self, request):
        return Response({
            'message': 'Welcome to the REST API',
            'endpoints': {
                'list of products': '/products/',
                'create a new product': '/create/',
                'detailed product view': '/products/<int:pk>/',
                'delete  product': '/products/<int:pk>/delete/',
                'update product': '/products/<int:pk>/update/',
            }
        })


class MyPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


# Create-product endpoint
class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Detailed-information endpoint
class DetailedProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Product listing endpoint
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = MyPagination


# Endpoint to delete the product
class DeleteProductView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# Endpoint to update the product (only stock can be changed)
class UpdateProductView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = UpdateProductStockSerializer

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
