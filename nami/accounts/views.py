from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        id_number = request.POST.get('id_number')
        cr_number = request.POST.get('cr_number')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        select_resident = request.POST.get('select_resident')

        user = User.objects.create_user(username=uname, password=password)
        user.profile.id_number = id_number
        user.profile.cr_number = cr_number
        user.profile.phone_number = phone_number
        user.profile.select_resident = select_resident

        user.save()
        login(request, user)

    return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('signPage')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
            return redirect('login')
