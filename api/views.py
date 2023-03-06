from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
  """
  DRF API View
  """
  # instance = Product.objects.all().order_by("?").first()
  # data = {}
  # if instance:
  #   # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
  #   data = ProductSerializer(instance).data
  return Response({"view": "API view"})

# @api_view(["POST"])
# def api_home(request, *args, **kwargs):
#   """
#   DRF API View
#   """
#   data = request.data
#   serializer = ProductSerializer(data=request.data)
#   if serializer.is_valid(raise_exception=True):
#     # instance = serializer.save()
#     print(serializer.data)
#   return Response(serializer.data)