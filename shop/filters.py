import django_filters
from shop.models import *

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
   
        fields = ['name','category','price','color_product','color']
            
            
            
        