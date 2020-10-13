from django import template

register = template.Library()


@register.filter
def is_my_page(value):
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


@register.filter
def not_auth_page(value):
    auth_pages = ('/login/', '/logout/', '/signup/')
    if value in auth_pages:
        return False
    return True
