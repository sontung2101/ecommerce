from django import template
from product.models import *

register = template.Library()


@register.filter
def getChild(parentId):
    return TypeProducts.objects.filter(type_parent=parentId)


@register.filter
def hasChild(parentId):
    childs = TypeProducts.objects.filter(type_parent=parentId)
    if childs is not None:
        if len(childs) > 0:
            return "True"
    return "False"
