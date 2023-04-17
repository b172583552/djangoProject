from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("welcome")


def users(request):
    return render(request, "user.html")


def tpl(request):
    name = "tom"
    roles = ["manager", "CEO", "security"]
    user_info = {'name': 'tom', 'salary': 100000, 'role': 'ceo'}
    return render(request, 'tpl.html', {"n1": name, 'n2': roles, 'n3': user_info})

def unicom(req):
    import requests
    res = requests.get()