from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # return super().perform_update(serializer)
        instance = serializer.save()
        if not instance.contetnt:
            instance.contetnt = instance.title

class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductGenericView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer

class ProductGenericCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        content = serializer.validated_data.get('contetnt') or None
        if content == None:
            content = serializer.validated_data.get('title')
        serializer.save(contetnt=content)