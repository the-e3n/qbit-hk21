from django import template

register = template.Library()


@register.filter(name='sub')
def sub(value, arg):
    print(value, arg)
    return value - arg


@register.filter(name='index')
def index(value, arg):
    return value[arg]


@register.filter(name='ldel')
def ldel(l1, l2, i):
    print(l1,l2)
    return l1[i]-l2[i]

