from django import template

register = template.Library()
@register.filter(name='cut')
#register.filter('cut',cut) #first arg is the name of the filter, second arg is the filter object itself

def cut(value,arg):
    """
    This Cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

