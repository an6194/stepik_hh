from django import template

register = template.Library()


@register.filter
def my_background(value):
    if value.startswith('/my'):
        return True
    return False


@register.filter
def my_user_menu(value):
    if value.startswith('/mycompany/vacanc'):
        return 2
    elif value.startswith('/mycompan'):
        return 1
    return 0
