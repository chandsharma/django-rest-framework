# import json
from django.http import JsonResponse, HttpRequest
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def test_api(request, *args, **kwargs):
    post_product = ProductSerializer(data = request.data)
    if post_product.is_valid(raise_exception=True):
        post_product.save()
        print(post_product.data)
        return Response(post_product.data)
    return Response({"err":"inld"},status=400)









# @api_view(["POST"])
def test_api1(request, *args, **kwargs):
    product  = Product.objects.all().order_by("?").first()
    data = {}
    if product:
        # data = model_to_dict(product)
        data = ProductSerializer(product).data
    return JsonResponse(data)