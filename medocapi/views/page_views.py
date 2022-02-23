from django.shortcuts import render


def page_principale(request):
    datas = {}
    return render(request, "pages/index.html", datas)


def detail_page(request, code):
    datas = {"code": code}

    return render(request, "pages/detail-medoc.html", datas)
