from .models import Brand, Mobile


def list_all_brands():
    query = Brand.objects.all()
    return query


def list_all_mobiles():
    query = Mobile.objects.all()
    return query


def price_of_mobile_with_model(model):
    query = Mobile.objects.get(model=model).price
    return query


def most_expensive_mobile():
    query = Mobile.objects.all().order_by("-price").first()
    return query


def all_mobiles_with_brand_of(brand_name):
    query = Mobile.objects.filter(brand__name=brand_name)
    return query


def all_available_mobiles_with_price_in_range(min_price, max_price):
    query = Mobile.objects.filter(
        is_available=True, price__gte=min_price, price__lte=max_price
    ).count()
    return query
