def my_pages(request):
    if request.path.startswith('/my'):
        flag = True
    else:
        flag = False
    return {
        'my_page': flag
    }
