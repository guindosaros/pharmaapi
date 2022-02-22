from django.shortcuts import render


def page_principale(request):
    datas = {}
    return render(request, "pages/index.html", datas)
