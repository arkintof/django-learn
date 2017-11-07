from django import template

register = template.Library()

@register.filter(name='modulo')
def modulo(val,num):
    return val