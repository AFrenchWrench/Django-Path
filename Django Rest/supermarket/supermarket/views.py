from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product


@api_view(["POST"])
def create_product(request):
    data = request.data
    product = Product.objects.create(name=data.get("name"), price=data.get("price"))
    return Response(
        {
            "message": "new product added successfully",
            "product": {"name": product.name, "price": product.price},
        },
        status=status.HTTP_201_CREATED,  # return message & product details
    )


@api_view(["GET"])
def get_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return Response(
        {"name": product.name, "price": product.price}, status=status.HTTP_200_OK
    )  # return product details
