from django import template
from shop.models import *

register = template.Library()


@register.inclusion_tag('shop/list_articles.html')
def show_articles(sort=None, cat_selected=0):
    if not sort:
        cats = Article.objects.all()
    else:
        cats = Article.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}