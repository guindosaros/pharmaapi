from django.shortcuts import render


def page_principale(request):
    datas = {}
    return render(request, "pages/pharma/index.html", datas)


def detail_page(request, code):
    datas = {"code": code}

    return render(request, "pages/pharma/detail-medoc.html", datas)


def category_page(request):
    datas = {}

    return render(request, "pages/shop/category.html", datas)
