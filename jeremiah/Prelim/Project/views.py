from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, AddAdminForm


# ================================
# LOGIN VIEW
# ================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('dashboard')

    return render(request, 'login.html', {'form': form})


# ================================
# DASHBOARD
# ================================

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# ================================
# ADD ADMIN
# ================================

@login_required
def add_admin(request):

    if request.method == "POST":
        form = AddAdminForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = AddAdminForm()

    return render(request, 'add_admin.html', {'form': form})


# ================================
# LOGOUT
# ================================

def logout_view(request):
    logout(request)
    return redirect('login')

