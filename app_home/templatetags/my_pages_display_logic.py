from django import template

register = template.Library()


@register.filter
def startswith(value, arg):
    if value.startswith(arg):
        return True
    return False


@register.filter
def not_auth_page(value):
    auth_pages = ('/login/', '/logout/', '/signup/')
    if value in auth_pages:
        return False
    return True
