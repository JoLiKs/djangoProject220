from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')
def profile(request):

    return render(request, 'profile.html')
@csrf_exempt
def login(request):
    if request.method == 'GET':
        name = 'Egoor'
        return render(request, 'login.html', {'user': name})
    if request.method == 'POST':
        loginn = request.POST['login']
        password = request.POST['password']
        mail = request.POST['email']
        return redirect('/profile/')
        #return HttpResponse(f'Авторизация прошла успешно\nLogin: {loginn} Password: {password} Email: {mail}')
    return HttpResponse('Такой запрос непредусмотрен')
