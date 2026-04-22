from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Vendor, Product, Inventory
from .services import normalize
from .models import Inventory
from django.db.models import Sum



@api_view(['GET'])
def sync_data(request):
    data = normalize()

    for item in data:
        vendor, _ = Vendor.objects.get_or_create(name=item["vendor_name"])
        product, _ = Product.objects.get_or_create(
            product_name=item["product_name"])

        Inventory.objects.update_or_create(
            product=product,
            vendor=vendor,
            defaults={
                "price": item["price"],
                "stock": item["stock"]
            }
        )

    return Response({"message": "Data Synced Successfully"})


@api_view(['GET'])
def get_products(request):
    name = request.GET.get('name')   # get query param

    data = Inventory.objects.select_related('product', 'vendor')

    # 🔍 Apply search filter
    if name:
        data = data.filter(product__product_name__icontains=name)

    result = []
    for i in data:
        result.append({
            "product_name": i.product.product_name,
            "vendor": i.vendor.name,
            "price": i.price,
            "stock": i.stock
        })

    return Response(result)


@api_view(['GET'])
def get_products_by_vendor(request, vendor_name):
    data = Inventory.objects.select_related('product', 'vendor') \
                            .filter(vendor__name__iexact=vendor_name)

    result = []
    for i in data:
        result.append({
            "product_name": i.product.product_name,
            "vendor": i.vendor.name,
            "price": i.price,
            "stock": i.stock
        })

    return Response(result)


@api_view(['POST'])
def add_inventory(request):
    data = request.data

    vendor, _ = Vendor.objects.get_or_create(name=data["vendor"])
    product, _ = Product.objects.get_or_create(product_name=data["product"])

    inventory = Inventory.objects.create(
        vendor=vendor,
        product=product,
        price=data["price"],
        stock=data["stock"]
    )

    return Response({"message": "Data Added Successfully"})


def dashboard(request):
    total_products = Product.objects.count()
    total_vendors = Vendor.objects.count()
    total_stock = Inventory.objects.aggregate(total=Sum('stock'))['total'] or 0
    low_stock = Inventory.objects.filter(stock__lt=5).count()

    context = {
        "total_products": total_products,
        "total_vendors": total_vendors,
        "total_stock": total_stock,
        "low_stock": low_stock,
    }

    return render(request, "inventory/dashboard.html", context)




def product_page(request):
    name = request.GET.get('name')
    data = Inventory.objects.select_related('product', 'vendor').order_by('id')

    if name:
        data = data.filter(product__product_name__icontains=name)

    return render(request, "inventory/products.html", {"data": data})
