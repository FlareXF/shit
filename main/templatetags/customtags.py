from django import template

register = template.Library()

@register.filter(name='dict_range')
def filter_dict_range(a, stroke):
    return range(a ,len(stroke.values))

@register.filter(name='get_key')
def filter_get_key(dictionary, i):
    return list(dictionary.values.keys())[i]

@register.filter(name='get_value')
def filter_get_value(dictionary, i):
    #print(list(dictionary.values.values())[i][j])
    return list(dictionary.values.values())[i]

@register.filter(name='multiply')
def filter_multiply(number, n):
    return number*n