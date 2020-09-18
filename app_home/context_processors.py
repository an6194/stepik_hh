def my_pages(request):
    if request.path.startswith('/mycompany/vacanc'):
        back = True
        vacancy = True
        company = False
    elif request.path.startswith('/mycompan'):
        back = True
        vacancy = False
        company = True
    else:
        back = False
        vacancy = False
        company = False
    return {
        'my_page': back,
        'my_company_page': company,
        'my_vacancy_page': vacancy
    }
