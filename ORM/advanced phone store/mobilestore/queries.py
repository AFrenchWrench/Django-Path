from .models import Brand, Mobile
from django.db.models import Q, F


def all_brands_not_in_korea_china():
    return Brand.objects.filter(~Q(nationality="Korea") & ~Q(nationality="China"))


def some_brand_mobiles(*brand_names):
    if not brand_names:
        return Mobile.objects.all()
    return Mobile.objects.filter(brand__name__in=brand_names)


def mobiles_brand_nation_equals_made_in():
    return Mobile.objects.filter(made_in=F("brand__nationality"))
