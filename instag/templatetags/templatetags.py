from django import template
from instag.models import Post
register = template.Library()

@register.filter(name='split')
def split(string,seperator):
    return string.split(seperator)[0]
