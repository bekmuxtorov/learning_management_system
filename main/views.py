from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import NewUserForm, EditProfileForm
from .models import Department, Topic


@login_required(login_url='/login')
def home_view(request):
    departments = Department.objects.all()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumotlar muvaffaqiyatli saqlandi.")
            return redirect("home")

    context = {
        'departments': departments
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login')
def detail_view(request, pk):
    topic = Topic.objects.get(pk=pk)
    departments = Department.objects.all()
    context = {
        'topic': topic,
        'departments': departments
    }
    return render(request, 'detail_topic.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Muafaqqiyatli ro'yhatdan o'tdingiz.")
            return redirect("home")
        messages.error(
            request, "Muvaffaqiyatsiz ro'yxatdan o'tish. Yaroqsiz maʼlumot.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(
                    request, "Foydalanuvchi nomi yoki parol noto‘g‘ri.")
        else:
            messages.error(
                request, "Foydalanuvchi nomi yoki parol noto‘g‘ri..")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return redirect("login")


def my_view(request):
    query = request.GET.get('q')
    if query:
        instances = Topic.objects.filter(
            Q(titleicontains=query) | Q(bodyicontains=query) |
            Q(department__name__icontains=query) | Q(bodyicontains=query)
        )
    else:
        instances = Topic.objects.none()

    context = {'instances': instances}
    return render(request, 'search_results.html', context)
