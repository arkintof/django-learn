from django import template

register = template.Library()

@register.filter
def modulo(val,num):
    return val % num