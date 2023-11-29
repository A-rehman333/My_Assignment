from django.shortcuts import render


def index(request):

    return render(request, "index.html")

def show(request):

    vl1 = request.GET['name']

    output={'name': vl1,
            }
    return render(request, "show.html", output)